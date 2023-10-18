class BaseDB:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value
        return

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return "key not found"

    def delete(self, key):
        if key in self.data:
            del self.data[key]

    def keys(self):
        return list(self.data.keys())

    def exists(self, key):
        if key in self.data:
            return True
        else:
            return False
