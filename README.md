# Boredom recognition app

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
  


