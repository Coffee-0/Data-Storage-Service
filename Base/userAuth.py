from hashlib import sha256


class UserAuth:
    def __init__(self, database):
        self.database = database
        self.salt = "/-_#*,+!?()=:.@"

    def createUser(self, username, password):
        if self.database.exists(username):
            print("user already exists")
            return

        hashedPassword = self.hashPassword(password)
        self.database.set(username, hashedPassword)
        print("user created successfully")
        return True

    def authenticateUser(self, username, password):
        if not self.database.exists(username):
            print("user does not exist")
            return False

        storedPassword = self.database.get(username)

        enteredPassword = self.hashPassword(password)
        if enteredPassword == storedPassword:
            print("Authentication successful")
            return True
        else:
            print("Incorrect Password")
            return False

    def hashPassword(self, password):
        saltedPasswrod = password + self.salt
        return sha256(saltedPasswrod.encode()).hexdigest()
