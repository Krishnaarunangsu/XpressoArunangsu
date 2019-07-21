# import pymongo


# Making a Connection with MongoClient
# The first step when working with PyMongo is to create a MongoClient to the running mongod instance

from pymongo import MongoClient

# The above code will connect on the default host and port.
client = MongoClient()


# We can also specify the host and port explicitly, as follows:
client = MongoClient('localhost', 27017)

# Or use the MongoDB URI format:
client = MongoClient('mongodb://localhost:27017/')

# Getting a Database
# A single instance of MongoDB can support multiple independent databases.
# When working with PyMongo you access databases using attribute style access on MongoClient instances:

db = client.test_database
# If your database name is such that using attribute style access won’t work (like test-database),
# you can use dictionary style access instead:
db = client['test-database']
# Getting a Collection
# A collection is a group of documents stored in MongoDB, and can be thought of as roughly the equivalent of a table
# in a relational database. Getting a collection in PyMongo works the same as getting a database:

collection = db.test_collection
# or (using dictionary style access):

collection = db['test-collection']
# An important note about collections (and databases) in MongoDB is that they are created lazily
# - none of the above commands have actually performed any operations on the MongoDB server.
# Collections and databases are created when the first document is inserted into them.

# https://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_connecting_accessing.php
# https://api.mongodb.com/python/current/tutorial.html
# http://bsonspec.org/
# https://dzone.com/articles/getting-started-with-python-and-mongodb
# https://realpython.com/introduction-to-mongodb-and-python/
