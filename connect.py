import pymongo

#open mongodb connection
connMongo = pymongo.Connection('mongodb://localhost:27017')

#print the databases
print connMongo.database_names()

#close the connection
connMongo.close()

