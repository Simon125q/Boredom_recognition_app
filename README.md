# Focus Guard

**Focus Guard** is a Python-based application designed to help users stay focused during online classes and courses. By monitoring facial landmarks, body posture, and user activity through the camera, the app detects signs of distraction such as closed eyes, yawning, or slouching. It encourages users to regain focus by using **gamification techniques**, offering fun and interactive mini-games when attention lapses are detected. Users can earn or lose points based on their focus levels, and detailed statistics about learning habits and progress are tracked over time.

## Features

### Focus Monitoring
- **Eye and Mouth Detection**: Uses the **MediaPipe** library to detect if the user's eyes are closed or if they are yawning.
  - **EAR (Eye Aspect Ratio)**: Measures how open the user's eyes are.
  - **MAR (Mouth Aspect Ratio)**: Measures the degree of yawning.
- **Posture Detection**: Checks if the user is sitting straight by using pose landmarks from **MediaPipe**, combined with a **Random Forest model** (trained with **scikit-learn**) to classify good and bad posture.

### Gamification
- **Mini-Games for Regaining Focus**: When the app detects that the user is distracted, mini-games are triggered to bring attention back to learning. These games include:
  - **Snake**: Control a snake and eat food while avoiding hitting the walls.
  - **Memory**: Find pairs of matching cards.
  - **Connect the Dots**: Draw a line connecting dots in a specific order.
  - **Physical Activities**: Simple exercises to encourage physical movement.
  - **Quick Alarm**: A user needs to stop an alarm as quickly as possible to minimize point loss.

### Points System and Statistics
- **Points System**: Users earn points for staying focused and lose points when distractions are detected. If a distraction occurs, playing a mini-game can help regain some of the lost points.
- **Statistics Page**:
  - Displays user's current level (based on total points accumulated).
  - Shows detailed statistics on time spent learning and points earned each day.
  
### User Interface
- **Custom Tkinter GUI**: The application features an easy-to-use graphical user interface built using **Tkinter**, offering access to all functions such as starting focus sessions, viewing statistics, and playing mini-games.

## Tech Stack

### Libraries and Tools
- **Python**: Core language used for building the application.
- **OpenCV**: For capturing live camera footage.
- **MediaPipe**: For detecting facial landmarks (eyes, mouth) and body posture in real-time.
- **scikit-learn**: To implement a Random Forest model that classifies posture based on pose landmarks from MediaPipe.
- **Tkinter**: For building the graphical user interface (GUI) and mini-games.
- **Pandas & Matplotlib**: For data storage, tracking focus history, and plotting learning statistics.

## How It Works

1. **Focus Detection**:
   - The app continuously monitors the user's face and body using the camera.
   - The **EAR (Eye Aspect Ratio)** is calculated to check if the eyes are open, and **MAR (Mouth Aspect Ratio)** to detect yawning.
   - The user’s posture is analyzed through body pose landmarks, and the **Random Forest model** classifies if the user is sitting straight.

2. **Distraction Detection**:
   - If the app detects signs of distraction (eyes closed, yawning, slouching), points are deducted, and a mini-game is triggered.

3. **Mini-Games**:
   - The user plays a mini-game that aims to re-engage attention. Winning or completing a mini-game helps the user regain some of the lost points.

4. **Statistics Tracking**:
   - The app tracks and records the user's focus performance, providing detailed insights on how long they spent learning, how many points they earned/lost, and overall progress through a **user level** system.

## Installation

To run this project locally, you need to have Python installed.

1. Clone the repository
2. Install required pacages:
   ```
   pip -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
   if it doesn't work go through steps 4-9 and if it does go to step 10.
4. Install anaconda
5. Open anaconda prompt and navigate to the app folder
6. Create new environment using:
   ```
   conda create --name <name> --file conda_env.txt
   ```
7. Now activate the environment:
   ```
   conda activate <name>
   ```
8. Using pip install additional pacgages:
   ```
   pip install pygame
   pip install customtkinter
   pip install mediapipe
   ```
9. Run the app:
   ```
   python app.py
   ```
10. To fine tune the model first run
   ```
   python DataColector.py
   ```
in order to collect new data. Next run
   ```
   python ModelTrainer.py
   ```
to train the model

### Mini-Games

The mini-games will automatically appear when the app detects a loss of focus. The games are easy to play and designed to re-engage the user. After playing, points are recalculated based on performance.

## Usage

- **Start Focus Session**: Click the "Start Focus" button to begin tracking your attention. The app will run in the background and alert you if distractions are detected.
- **View Statistics**: Use the "Statistics" button to view your learning performance, including daily focus points, time spent on learning, and your current level.
- **Mini-Games**: These will appear automatically during a focus session if the app detects you are losing attention. Try to win the games to regain lost focus points. You can customize which mini-games will be shown to you as well as they frequency in a settings page.


