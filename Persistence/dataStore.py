import json


class BaseDB:
    def __init__(self, data_file="data.json"):
        self.data_file = data_file
        self.data = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.data, file)

    def set(self, key, value):
        self.data[key] = value
        self.save_data()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save_data()

    def get(self, key):
        return self.data.get(key)

    def keys(self):
        return list(self.data.keys())

    def exists(self, key):
        return key in self.data
