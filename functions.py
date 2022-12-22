import json
from api_calls import getRankInfo
from summonerClass import *

#takes json obj and turns it into a string
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#takes in endpoint response prints out info
def PrintStatus(obj):
    print(obj.status_code)
    print(obj.json)

#{'name': name, 'puuid': puuid, 'e_id': encrypted_id, 'champ': champ, 'kills':kills, 'deaths': deaths, 'assists':assists}
#returns a dictionary for each player in an inputted match, formated as above statement
#pass in a json dictionary of the match
def createPlayerDictionary(match):
    summoner_dict = {}
    # x is a single summoner
    for x in range(10):
        summoner_dict[x] = {'name': match.json()['info']['participants'][x]['summonerName'],
        'puuid':match.json()['info']['participants'][x]['puuid'],
        'e_id': match.json()['info']['participants'][x]['summonerId'],
        'champ': match.json()['info']['participants'][x]['championName'],
        'kills': match.json()['info']['participants'][x]['kills'],
        'deaths': match.json()['info']['participants'][x]['deaths'],
        'assists': match.json()['info']['participants'][x]['assists']}
    summoner_dict[10] = {'blue_win': match.json()['info']['teams'][0]['win'],
    'red_win': match.json()['info']['teams'][1]['win']}
    return summoner_dict

def createPlayerClasses(match):
    list = []
    for x in range(10):
        list[x] = Summoner(match.json()['info']['participants'][x]['summonerName'],
        match.json()['info']['participants'][x]['puuid'],
        match.json()['info']['participants'][x]['summonerId'],
        match.json()['info']['participants'][x]['championName'],
        match.json()['info']['participants'][x]['kills'],
        match.json()['info']['participants'][x]['deaths'],
        match.json()['info']['participants'][x]['assists'])
    return list

#prints players in a match by taking in a dictionary
def printPlayers(dict):
    #print("players in latest match:")
    print("blue team win: ", dict[10]['blue_win'])
    for i in range(5):
        print(dict[i]['name'] + ": " + dict[i]['champ'] + " " + str(dict[i]['kills']) + "/" + str(dict[i]['deaths']) + "/" + str(dict[i]['assists']))
    print("\nred team win: ", dict[10]['red_win'])
    for j in range(5, 10):
        print(dict[j]['name'] + ": " + dict[j]['champ'] + " " + str(dict[j]['kills']) + "/" + str(dict[j]['deaths']) + "/" + str(dict[j]['assists']))


#
#def getRanks(dict):
#    for i in range(10):
#        rank_json = getRankInfo(dict[i]['e_id'])
