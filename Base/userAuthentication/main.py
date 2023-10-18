from getpass import getpass

from base import BaseDB
from userAuth import UserAuth

database = BaseDB()
auth = UserAuth(database)


while True:
    print("\nOptions:")
    print("1. Create a new user")
    print("2. Authenticate a user")
    print("3. Quit")

    choice = int(input("Awaiting user Option : "))

    if choice == 1:
        print("Creating User\n")
        user = input("Enter Username : ")
        passwd = getpass("Enter Password : ")
        auth.createUser(username=user, password=passwd)

    elif choice == 2:
        print("Authorizing User\n")
        user = input("Enter Username : ")
        passwd = getpass("Enter Password : ")
        auth.authenticateUser(username=user, password=passwd)

    elif choice == 3:
        print("session ended")
        break

    else:
        print("Enter a valid option")
