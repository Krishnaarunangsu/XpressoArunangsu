import pymongo
from pymongo import MongoClient

# The above code will connect on the default host and port.
# client = MongoClient()


# We can also specify the host and port explicitly, as follows:
#client = MongoClient('localhost', 27017)


DB_USER = 'abzAdmin'
DB_PASS = 'Abz00ba1nc'
DB_MACHINE = 'localhost'
DB_PORT = 27017
DB_SOURCE = 'mydb1'
# Or use the MongoDB URI format:
#client = MongoClient('mongodb://username:password@localhost:27017/')


client = MongoClient(DB_MACHINE, DB_PORT)
db = client.db_name
if db.authenticate(DB_USER, DB_PASS, source=DB_SOURCE):
    print('Trust in God')

else:
    print('Connection Failed')
