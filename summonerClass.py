class Summoner:
    def __init__(self, name, puuid, e_id, champ, kills, deaths, assists) -> None:
        self.name = name
        self.puuid = puuid
        self.e_id = e_id
        self.champ = champ
        self.kills = kills
        self.deaths = deaths
        self.assists = assists