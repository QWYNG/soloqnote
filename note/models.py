from django.db import models
from riotwatcher import RiotWatcher
from requests import HTTPError
import json
import collections
# Create your models here.
class SNset():

    def lol(self,summoner_name_data):

        watcher = RiotWatcher('RGAPI-ee54c73d-6709-4623-bd24-42346712bb4d')
        my_region = 'jp1'
        me = watcher.summoner.by_name(my_region, summoner_name_data)
        my_ranked_stats  = watcher.league.positions_by_summoner(my_region, me['id'])
        recentmatchlists = watcher.match.matchlist_by_account_recent(my_region,me[ 'accountId'])
        matches = recentmatchlists['matches']
        x = 0
        match_detail = []
        for x in range(20):
            match_detail.append(watcher.match.by_id(my_region, matches[x]['gameId']))
            x += 1
        for my_ranked_stat in my_ranked_stats:
            dict = {'my_ranked_stat': my_ranked_stat, 'me': me,"recentmatchlists":recentmatchlists,'match_detail':match_detail}
        return (dict)
