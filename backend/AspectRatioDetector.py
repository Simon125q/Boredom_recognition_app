import numpy as np
import pandas as pd
import mediapipe as mp
from settings import *


class AspectRatioDetector:
    def __init__(self) -> None:
        self.chosen_left_eye_idxs  = [362, 385, 387, 263, 373, 380]
        self.chosen_right_eye_idxs = [33,  160, 158, 133, 153, 144]
        self.chosen_mouth_idxs = [61, 306, 13, 14]
	
    def distance(self, point_1, point_2):
        """Calculate l2-norm between two points"""
        dist = sum([(i - j) ** 2 for i, j in zip(point_1, point_2)]) ** 0.5
        return dist
    
    def get_ear(self, landmarks, refer_idxs):
        """
        Calculate Eye Aspect Ratio for one eye.
    
        Args:
            landmarks: (list) Detected landmarks list
            refer_idxs: (list) Index positions of the chosen landmarks
                                in order P1, P2, P3, P4, P5, P6
            frame_width: (int) Width of captured frame
            frame_height: (int) Height of captured frame
    
        Returns:
            ear: (float) Eye aspect ratio
        """
    
        try:
            # Compute the euclidean distance between the horizontal
            coords_points = []
            for i in refer_idxs:
                lm = landmarks[i]
                coord = (lm.x, lm.y)
                coords_points.append(coord)
            
            # Eye landmark (x, y)-coordinates
            P2_P6 = self.distance(coords_points[1], coords_points[5])
            P3_P5 = self.distance(coords_points[2], coords_points[4])
            P1_P4 = self.distance(coords_points[0], coords_points[3])
            
            # Compute the eye aspect ratio
            ear = (P2_P6 + P3_P5) / (2.0 * P1_P4)
        except:
            ear = 0.0
            coords_points = None
    
        return ear, coords_points
    
    def calculate_avg_ear(self, landmarks, left_eye_idxs, right_eye_idxs):
        """Calculate Eye aspect ratio"""
        
        left_ear, left_lm_coordinates = self.get_ear(
                                        landmarks, 
                                        left_eye_idxs
                                        )
        right_ear, right_lm_coordinates = self.get_ear(
                                        landmarks, 
                                        right_eye_idxs
                                        )
        Avg_EAR = (left_ear + right_ear) / 2.0
    
        return Avg_EAR
    
    def calculculate_mar(self, landmarks) -> float:
        try:
            # Compute the euclidean distance between the horizontal
            coords_points = []
            for i in self.chosen_mouth_idxs:
                lm = landmarks[i]
                coord = (lm.x, lm.y)
                coords_points.append(coord)
            
            # Eye landmark (x, y)-coordinates
            P1_P2 = self.distance(coords_points[0], coords_points[1])
            P3_P4 = self.distance(coords_points[2], coords_points[3])
            
            # Compute the eye aspect ratio
            mar = P3_P4 / P1_P2
        except:
            mar = 0.0
            coords_points = None
    
        return mar
    
    def check_mouth(self, mar: float) -> str:
        if mar < MOUTH_CLOSED:
            return "closed"
        else:
            return "open"

    def check_eyes(self, ear: float) -> str:
        if ear < EYES_SQUINTED:
            if ear < EYES_CLOSED:
                return "closed"
            else:
                return "squinted"
        else:
            return "open"
        
    def detect_ear(self, face_landmarks) -> tuple[float, str]:
        
        ear_ratio: float = self.calculate_avg_ear(face_landmarks.landmark, self.chosen_left_eye_idxs, self.chosen_right_eye_idxs)
        eyes: str = self.check_eyes(ear_ratio)
        return (ear_ratio, eyes)
    
    def detect_mar(self, face_landmarks) -> tuple[float, str]:

        mar_ratio = self.calculculate_mar(face_landmarks.landmark)
        mouth: str = self.check_mouth(mar_ratio)
        return (mar_ratio, mouth)