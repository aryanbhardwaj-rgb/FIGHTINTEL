import json
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

TRAINING_FILE = "training_data.json"

class AIMovePredictor:
    def __init__(self):
        self.model = KNeighborsClassifier(n_neighbors=1)
        self.move_map = {"LEFT": 0, "RIGHT": 1, "JUMP": 2, "PUNCH": 3}
        self.reverse_map = {v: k for k, v in self.move_map.items()}
        self.X = []
        self.y = []
        self.load_data()

    def encode(self, moves):
        return [self.move_map.get(move, -1) for move in moves]

    def load_data(self):
        try:
            with open(TRAINING_FILE, "r") as f:
                data = json.load(f)
            for item in data:
                self.X.append(self.encode(item["input"]))
                self.y.append(self.move_map.get(item["output"], -1))
            if self.X:
                self.model.fit(self.X, self.y)
        except Exception as e:
            print("AI Model Load Error:", e)

    def save_training_data(self, input_moves, next_move):
        try:
            with open(TRAINING_FILE, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append({"input": input_moves, "output": next_move})

        with open(TRAINING_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def train(self):
        if self.X and self.y:
            self.model.fit(self.X, self.y)

    def predict(self, input_moves):
        if len(self.X) < 1:
            return None
        encoded = self.encode(input_moves)
        if -1 in encoded:
            return None
        try:
            prediction = self.model.predict([encoded])[0]
            return self.reverse_map.get(prediction, None)
        except:
            return None