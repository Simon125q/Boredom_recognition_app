import json
from enum import Enum

def importSettings() -> dict:
    with open("mySettings.json", "r") as settingsFile:
       settings = json.load(settingsFile)
    return settings

# model tuning parameters tresholds
EYES_SQUINTED = 0.30
EYES_CLOSED = 0.24

MOUTH_CLOSED = 0.30

# name of the CSV file containing collected data
CSV_FILE_NAME = "coords"
RANDOM_FOREST_MODEL = "models/rf_model.pkl"

# Detected mesh colors
FACE_DOTS_COLOR = (80,110,10)
FACE_CONNECTIONS_COLOR = (80,256,121)
POSE_DOTS_COLOR = (245,117,66)
POSE_CONNECTIONS_COLOR = (245,66,230)
RIGHT_HAND_DOTS_COLOR = (80,22,10)
RIGHT_HAND_CONNECTIONS_COLOR = (80,44,121)
LEFT_HAND_DOTS_COLOR = (121,22,76)
LEFT_HAND_CONNECTIONS_COLOR = (121,44,250)

#App look
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT) = (1250, 750)
TITLE = "Focus Guard"
APP_NAME = "Focus Guard"

# User settings
SETTINGS = importSettings()
""" TIME_BETWEEN_GAMES = 30
CONNECT_DOTS_ENABLE = True
EXCERCISE_ENABLE = True
SNAKE_ENABLE = False
MEMORY_ENABLE = False
ALARM_ENABLE = False """

class GameType(Enum):
    DOTS = 1
    EXCERCISE = 2
    SNAKE = 3
    MEMORY = 4
    ALARM = 5
    TICTACTOE = 6
