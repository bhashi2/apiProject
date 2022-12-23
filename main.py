import requests
import json
from functions import *
from api_calls import *
from summonerClass import *

name = "Viollet" 
# name = input("summoner name: ")

#takes in name and gives it to the endpoint
sum_details = getSummoner(name)

#print(sum_details.json()['name'])
puuid = sum_details.json()['puuid']
encrypted_id = sum_details.json()['id']
#print(puuid)

match_ids = getMatchIds(puuid, "10")

#print(match_ids.json()[0])

# prints recent matches
for i in range(1):
    print("match number:", i+1)
    match = getMatchInfo(match_ids.json()[i])
    summoner_dict = createMatchDictionary(match)

    printPlayers(summoner_dict)
    # print(summoner_dict)
    print("\n")

# rank_json = getRankInfo(summoner_dict[0]['e_id'])

# rank = rank_json.json()[0]['tier']
# print(rank)