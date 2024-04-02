import pickle
import numpy as np
import pandas as pd


class PoseDetector:
    def __init__(self, model_path) -> None:
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def extract_data(self, pose_landmarks, face_landmarks) -> pd.DataFrame:
        # Extract Pose landmarks
        pose = pose_landmarks.landmark
        pose_row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in pose]).flatten())
        
        # Extract Face landmarks
        face = face_landmarks.landmark
        face_row = list(np.array([[landmark.x, landmark.y, landmark.z, landmark.visibility] for landmark in face]).flatten())
        
        # Concate rows
        row = pose_row + face_row

        return pd.DataFrame([row])

    def detect(self, pose_landmarks, face_landmarks) -> tuple[str, float]:
        # Make Detections
        X = self.extract_data(pose_landmarks, face_landmarks)
        body_language_class = self.model.predict(X)[0]
        body_language_prob = self.model.predict_proba(X)[0]
        body_language_prob = round(body_language_prob[np.argmax(body_language_prob)],2)
        #print(body_language_class, body_language_prob)

        return (body_language_class, body_language_prob)
                                
            