from settings import *
from backend.PoseDetector import PoseDetector
import mediapipe as mp
import numpy as np
import cv2

class Detector:
    def __init__(self) -> None:
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic
        self.poseDetector = PoseDetector(RANDOM_FOREST_MODEL)
        pass

    def draw_landmarks(self, results, image) -> np.ndarray:
        self.mp_drawing.draw_landmarks(image, results.face_landmarks, self.mp_holistic.FACEMESH_TESSELATION, 
                                self.mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                                self.mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                                )
        
        # 2. Right hand
        self.mp_drawing.draw_landmarks(image, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS, 
                                self.mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                                self.mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                                )

        # 3. Left Hand
        self.mp_drawing.draw_landmarks(image, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS, 
                                self.mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                                self.mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                                )

        # 4. Pose Detections
        self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS, 
                                self.mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                                self.mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                                )
        
        return image

    def draw_results(self, results, image, body_language_class: str, body_language_prob: float) -> np.ndarray:
        # Grab ear coords
        coords = tuple(np.multiply(
                        np.array(
                            (results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_EAR].x, 
                            results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_EAR].y))
                    , [640,480]).astype(int))
        
        cv2.rectangle(image, 
                    (coords[0], coords[1]+5), 
                    (coords[0]+len(body_language_class)*20, coords[1]-30), 
                    (245, 117, 16), -1)
        cv2.putText(image, body_language_class, coords, 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Get status box
        cv2.rectangle(image, (0,0), (250, 60), (245, 117, 16), -1)
        
        # Display Class
        cv2.putText(image, 'CLASS'
                    , (95,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, body_language_class.split(' ')[0]
                    , (90,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Display Probability
        cv2.putText(image, 'PROB'
                    , (15,12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(round(body_language_prob,2))
                    , (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        return image
        
    def start(self) -> None:
        
        cap = cv2.VideoCapture(0)
        # Initiate holistic model
        with self.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            while cap.isOpened():
                ret, frame = cap.read()
                
                # Recolor Feed
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False        
                
                # Make Detections
                results = holistic.process(image)
                
                # Recolor image back to BGR for rendering
                image.flags.writeable = True   
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                image = self.draw_landmarks(results, image)
                
                try:
                    body_language_class, body_language_prob = self.poseDetector.detect(results.pose_landmarks, results.face_landmarks)
                    
                    image = self.draw_results(results, image, body_language_class, body_language_prob)
                except:
                    pass
                                
                cv2.imshow('Raw Webcam Feed', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()