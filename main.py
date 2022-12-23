import requests
import json
import pymongo
from functions import *
from api_calls import *
from summonerClass import *
from mongodatabase import get_database

dbname = get_database()
myCol = dbname["matches"]
name = "Viollet" 
# name = input("summoner name: ")

#takes in name and gives it to the endpoint
sum_details = getSummoner(name)
#print(sum_details.json()['name'])
puuid = sum_details.json()['puuid']
encrypted_id = sum_details.json()['id']
#print(puuid)
match_ids = getMatchIds(puuid, "10")

# prints recent matches
for i in range(1):
    print("match number:", i+1)
    match = getMatchInfo(match_ids.json()[i])
    summoner_dict = createMatchDictionary(match)
    # for x in summoner_dict.values():
    #     print(x)
    printPlayers(summoner_dict)
    print("\n")
    # x = myCol.insert_one(summoner_dict)

# rank_json = getRankInfo(summoner_dict[0]['e_id'])

# rank = rank_json.json()[0]['tier']
# print(rank)