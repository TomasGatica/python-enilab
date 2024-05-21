from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = ""
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
try:
    database = client.get_database("sample_mflix")
    movies = database.get_collection("movies")
    
    # Query para una pelìcula que tiene el tìtulo: volver al futuro
    query = { "title": "Back to the Future" }
    movie = movies.find_one(query)
    print(movie)
    client.close()
    
    
except Exception as e:
    raise Exception("Incapaz de encontrar el documento, error:", e)

