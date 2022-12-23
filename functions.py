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
        summoner_dict[x] = {
        'name': match.json()['info']['participants'][x]['summonerName'],
        'puuid':match.json()['info']['participants'][x]['puuid'],
        'e_id': match.json()['info']['participants'][x]['summonerId'],
        'champ': match.json()['info']['participants'][x]['championName'],
        'kills': match.json()['info']['participants'][x]['kills'],
        'deaths': match.json()['info']['participants'][x]['deaths'],
        'assists': match.json()['info']['participants'][x]['assists']
        #'role': match.json()['info']['participants'][x]['lane']
        }
    return summoner_dict


#prints players in a match by taking in a dictionary and match info
def printPlayers(dict):
    print("game mode:",dict['gameMode'])
    print("team win:",dict['teamWin'])
    print("\nblue team: ")
    for i in range(5):
        print(dict[i]['name'] + ": " + dict[i]['champ'] + " " + str(dict[i]['kills']) + "/" + str(dict[i]['deaths']) + "/" + str(dict[i]['assists']))
    print("\nred team:")
    for j in range(5, 10):
        print(dict[j]['name'] + ": " + dict[j]['champ'] + " " + str(dict[j]['kills']) + "/" + str(dict[j]['deaths']) + "/" + str(dict[j]['assists']))

    



#
#def getRanks(dict):
#    for i in range(10):
#        rank_json = getRankInfo(dict[i]['e_id'])
