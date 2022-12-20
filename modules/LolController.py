from riotwatcher import LolWatcher, ApiError
from dotenv import load_dotenv
import os

load_dotenv()
RIOT_API_KEY = os.getenv('RIOT_API_KEY')
watcher = LolWatcher(RIOT_API_KEY)
region = 'EUN1'

class Summoner:
    def __init__(self, summonerName):
        self.summonerName = summonerName
        summoner_obj = watcher.summoner.by_name(region, self.summonerName)
        stats_obj = watcher.league.by_summoner(region, summoner_obj['id'])
        self.summoner_obj = summoner_obj
        self.stats_obj = stats_obj

    def getSummonerStats(self):
        stats = 'Summoner name: ' + self.summoner_obj['name'] + '\n'
        stats += 'Summoner level: ' + str(self.summoner_obj['summonerLevel']) + '\n'
        for i in self.stats_obj:
            if i['queueType'] == 'RANKED_SOLO_5x5':
                queueType = "Ranked Solo/Duo"
            elif i['queueType'] == 'RANKED_FLEX_SR':
                queueType = "Ranked Flex"
            else:
                queueType = i['queueType']
            stats += queueType + '\n'
            stats += '\tSummoner rank: ' + i['tier'] + ' ' + i['rank'] + '\n'
            stats += '\tSummoner LP: ' + str(i['leaguePoints']) + '\n'
            stats += '\tSummoner wins: ' + str(i['wins']) + '\n'
            stats += '\tSummoner losses: ' + str(i['losses']) + '\n'
            stats += '\tSummoner winrate: ' + str(round(i['wins'] / (i['wins'] + i['losses']) * 100, 2)) + '%' + '\n'
        return stats
