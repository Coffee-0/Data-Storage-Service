from dataStore import BaseDB

database = BaseDB()
# Add to DB
database.set("john", "wick")
k = database.keys()
print(k)
# Get from DB
value = database.get("john")
print(value)
# Delete from DB
database.delete("john")
k = database.keys()
print(k)
