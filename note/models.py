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
        dict = {'my_ranked_stats': my_ranked_stats[1], 'me': me}
        return (dict)
