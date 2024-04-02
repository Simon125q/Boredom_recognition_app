from fer import FER

class EmotionDetector:
    def __init__(self) -> None:
        #initialize the detector
        self.detector = FER(mtcnn=True)

    def detect(self, image) -> tuple[str, float]:
        result = self.detector.detect_emotions(image)
        face = result[0]
        
        emotions = face["emotions"]

        # Find emotion with the highest score
        emotion_type = max(emotions, key=emotions.get)
        emotion_score = round(emotions[emotion_type], 2)

        return (emotion_type, emotion_score)
