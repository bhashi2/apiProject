import requests
from api_key import *

#returns details of an account: acc id, id, name, icon id, puuid, revision date, summoner level
def getSummoner(name):
    sum_details = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + apiKey)
    return sum_details

#returns the recent match ids, m_num is the number of matches I want to pull and it must be a string
def getMatchIds(puuid, m_num):
    match_ids = requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=" + m_num + "&api_key=" + apiKey)
    return match_ids

#returns everything about a match: check sample match in stuff for example
#teamId: 100 is blue, 200 is red in teams array, also tells who won
def getMatchInfo(match_id):
    match = requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/" + match_id + "?api_key=" + apiKey)
    return match

#returns ranked information, check sample ranked in stuff for example
def getRankInfo(e_id):
     rank = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + e_id + api_req)
     return rank

#returns 404 if not in game, can use ig.status_code to get status code
#returns 200 and information about game if in game
def inGame(puuid):
    ig = requests.get("https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + puuid + api_req)
    return ig
