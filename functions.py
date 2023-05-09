import json
from api_calls import getRankInfo
from summonerClass import *

# takes json obj and turns it into a string
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# takes in endpoint response prints out info
def PrintStatus(obj):
    print(obj.status_code)
    print(obj.json)

# {'name': name, 'puuid': puuid, 'e_id': encrypted_id, 'champ': champ, 'kills':kills, 'deaths': deaths, 'assists':assists}
# returns a dictionary for each player in an inputted match, formated as above statement
# pass in a json dictionary of the match
def createMatchDictionary(match):
    summoner_dict = {
        'gameMode':match.json()['info']['gameMode'],
        'teamWin':'blue' if match.json()['info']['teams'][0]['win'] else 'red'
    }
    # x is each summoner dictionary, so x is the number of the key and value is summoner information
    for x in range(10):
        sum_key = "sum" + str(x)
        summoner_dict[sum_key] = {
        'name': match.json()['info']['participants'][x]['summonerName'],
        'puuid':match.json()['info']['participants'][x]['puuid'],
        'e_id': match.json()['info']['participants'][x]['summonerId'],
        'champ': match.json()['info']['participants'][x]['championName'],
        'kills': match.json()['info']['participants'][x]['kills'],
        'deaths': match.json()['info']['participants'][x]['deaths'],
        'assists': match.json()['info']['participants'][x]['assists'],
        'role': match.json()['info']['participants'][x]['teamPosition'],
        'cs':match.json()['info']['participants'][x]['totalMinionsKilled']
        }
    return summoner_dict


#prints players in a match by taking in a dictionary and match info
def printPlayers(dict):
    print("game mode:",dict['gameMode'])
    print("team win:",dict['teamWin'])
    print("\nblue team: ")
    for i in range(5):
        key = "sum" + str(i)
        print(dict[key]['role'] + " " + dict[key]['name'] + ": " + dict[key]['champ'] + " " + str(dict[key]['kills']) + "/" + str(dict[key]['deaths']) + "/" + str(dict[key]['assists']) + " cs:" + str(dict[key]['cs']))
    print("\nred team:")
    for j in range(5, 10):
        keyj = "sum" + str(j)
        print(dict[keyj]['role'] + " " + dict[keyj]['name'] + ": " + dict[keyj]['champ'] + " " + str(dict[keyj]['kills']) + "/" + str(dict[keyj]['deaths']) + "/" + str(dict[keyj]['assists']) + " cs:" + str(dict[keyj]['cs']))

    



#
#def getRanks(dict):
#    for i in range(10):
#        rank_json = getRankInfo(dict[i]['e_id'])
