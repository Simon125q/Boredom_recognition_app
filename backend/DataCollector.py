import mediapipe as mp
import cv2
import csv
import numpy as np
import os
import time


# name of the CSV file containing collected data
CSV_FILE_NAME = "coords"

# Detected mesh colors
FACE_DOTS_COLOR = (80,110,10)
FACE_CONNECTIONS_COLOR = (80,256,121)
POSE_DOTS_COLOR = (245,117,66)
POSE_CONNECTIONS_COLOR = (245,66,230)
RIGHT_HAND_DOTS_COLOR = (80,22,10)
RIGHT_HAND_CONNECTIONS_COLOR = (80,44,121)
LEFT_HAND_DOTS_COLOR = (121,22,76)
LEFT_HAND_CONNECTIONS_COLOR = (121,44,250)


class DataCollector():
    def __init__(self):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic
        self.class_name = ""

    def create_csv_file(self, results):
        num_coords = len(results.pose_landmarks.landmark) + len(results.face_landmarks.landmark)

        cols = ["class"]
        for val in range(1, num_coords + 1):
            cols += [f"x{val}", f"y{val}", f"z{val}", f"v{val}"]

        with open(CSV_FILE_NAME + '.csv', mode = 'w', newline = '') as f:
            csv_writer = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
            csv_writer.writerow(cols)

    def get_class_name(self):
        self.class_name = input("Enter name of the presenting expression: ").lower()

    def timer(self):
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("GO")
        time.sleep(0.3)

    def draw_landmarks(self, image, results) -> np.ndarray:
        # 1. Draw face landmarks
        self.mp_drawing.draw_landmarks(image, results.face_landmarks, self.mp_holistic.FACEMESH_TESSELATION, 
                                self.mp_drawing.DrawingSpec(color=FACE_CONNECTIONS_COLOR, thickness=1, circle_radius=1),
                                self.mp_drawing.DrawingSpec(color=FACE_DOTS_COLOR, thickness=1, circle_radius=1)
                                )
        
        # 2. Right hand
        self.mp_drawing.draw_landmarks(image, results.right_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS, 
                                self.mp_drawing.DrawingSpec(color=RIGHT_HAND_CONNECTIONS_COLOR, thickness=2, circle_radius=2),
                                self.mp_drawing.DrawingSpec(color=RIGHT_HAND_DOTS_COLOR, thickness=2, circle_radius=2)
                                )

        # 3. Left Hand
        self.mp_drawing.draw_landmarks(image, results.left_hand_landmarks, self.mp_holistic.HAND_CONNECTIONS, 
                                self.mp_drawing.DrawingSpec(color=LEFT_HAND_CONNECTIONS_COLOR, thickness=2, circle_radius=2),
                                self.mp_drawing.DrawingSpec(color=LEFT_HAND_DOTS_COLOR, thickness=2, circle_radius=2)
                                )

        # 4. Pose Detections
        self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS, 
                                self.mp_drawing.DrawingSpec(color=POSE_CONNECTIONS_COLOR, thickness=2, circle_radius=3),
                                self.mp_drawing.DrawingSpec(color=POSE_DOTS_COLOR, thickness=2, circle_radius=2)
                                )
        
        return image
    
    def add_data_to_csv(self, results):
        try:
            pose = results.pose_landmarks.landmark
            pose_row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())
            
            face = results.face_landmarks.landmark
            face_row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in face]).flatten())
            
            new_row = pose_row + face_row
            new_row.insert(0, self.class_name)
            
            try:
                with open(CSV_FILE_NAME + ".csv", mode = "a", newline = "") as f:
                    csv_writer = csv.writer(f, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                    csv_writer.writerow(new_row)
            except:
                self.create_csv_file()
                with open(CSV_FILE_NAME + ".csv", mode = "a", newline = "") as f:
                    csv_writer = csv.writer(f, delimiter = ",", quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                    csv_writer.writerow(new_row)        
        except:
            pass

    def video_capture(self):
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

                image.flags.writeable = True
                # Recolor image back to BGR for rendering
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                image = self.draw_landmarks(image, results)
                
                self.add_data_to_csv(results)
                
                cv2.imshow('Raw Webcam Feed', image)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

    def run(self):
        while True:
            self.get_class_name()
            self.timer()
            self.video_capture()
            x = input("Do you want to add another data? y/n ")
            if x.upper() == "N":
                break

if __name__ == "__main__":
    dataCollector = DataCollector()
    dataCollector.run()