import pymongo
from pymongo import MongoClient

# The above code will connect on the default host and port.
# client = MongoClient()


# We can also specify the host and port explicitly, as follows:
#client = MongoClient('localhost', 27017)

# "mongodb": {
#                 "mongo_url": "mongodb://172.16.3.1:27017/?replicaSet=rs0",
#                 "database": "xprdb",
#                 "mongo_uid": "xprdb_admin",
#                 "mongo_pwd": "xprdb@Abz00ba",
#                 "w": 1,
#                 "interval_between_retries": 5,
#                 "max_retries": 2
#         },

DB_USER = 'xprdb_admin'
DB_PASS = 'xprdb@Abz00ba'
DB_MACHINE = '172.16.3.1'
DB_PORT = 27017
DB_SOURCE = 'xprdb'

# *********************************************
# DB_USER = 'abzAdmin'
# DB_PASS = 'Abz00ba1nc'
# DB_MACHINE = 'localhost'
# DB_PORT = 27017
# DB_SOURCE = 'mydb1'
# Or use the MongoDB URI format:
#client = MongoClient('mongodb://username:password@localhost:27017/')


client = MongoClient(DB_MACHINE, DB_PORT)
db = client.db_name
if db.authenticate(DB_USER, DB_PASS, source=DB_SOURCE):
    print('MongoDB Connection is successful')

else:
    print('MongoDB Connection Failed')
