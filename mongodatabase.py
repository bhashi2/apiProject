from pymongo import MongoClient
from api_key import connectionString
def get_database():
    client = MongoClient(connectionString)
    return client['league_data']

if __name__ == "__main__":
    dbname = get_database()