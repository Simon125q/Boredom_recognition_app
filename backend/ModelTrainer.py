import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pickle

TEST_SET_FRACTION = 0.3

class ModelTrainer:
    def __init__(self, data_file_name) -> None:
        self.file_name = data_file_name
        self.pipelines = {
                            'lr': make_pipeline(StandardScaler(), LogisticRegression()),
                            'rc': make_pipeline(StandardScaler(), RidgeClassifier()),
                            'rf': make_pipeline(StandardScaler(), RandomForestClassifier()),
                            'gb': make_pipeline(StandardScaler(), GradientBoostingClassifier())
                        }
        self.fit_models = {}
        df = pd.read_csv(self.file_name)
        self.X = df.drop('class', axis = 1) # features
        self.y = df["class"] # target value

        # split data into training and test sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = TEST_SET_FRACTION, random_state = 1234)

    def train_models(self):
        for alg, pipeline in self.pipelines.items():
            print(alg)
            model = pipeline.fit(self.X_train, self.y_train)
            self.fit_models[alg] = model

    def evaluate_models(self):
        for alg, model in self.fit_models.items():
            yhat = model.predict(self.X_test)
            print(alg, accuracy_score(self.y_test, yhat))

    def save_models(self, path = ""):
        # save model
        for alg, model in self.fit_models.items():
            with open(str(path) + alg + "_model.pkl", 'wb') as f:
                pickle.dump(self.fit_models[alg], f)

    def run(self):
        self.train_models()
        self.evaluate_models()
        self.save_models()

if __name__ == "__main__":
    modelTrainer = ModelTrainer("coords.csv")
    modelTrainer.train_models()
    modelTrainer.evaluate_models()
    modelTrainer.save_models("models/")