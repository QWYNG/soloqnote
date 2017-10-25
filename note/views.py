from django.shortcuts import render
from riotwatcher import RiotWatcher
from django.http import HttpResponse
from requests import HTTPError
import json
from django.template.loader import render_to_string
from .forms import MyForm
# Create your views here.


def form_test(request):
        if request.method == "GET":
            form = MyForm(request.GET)
        if form.is_valid():
            summoner_name_data = form.cleaned_data['text'] # ← 受け取ったデータの正当性確認
            watcher = RiotWatcher('RGAPI-666f39a3-d412-4403-ad4e-11fa5c6b659f')
            my_region = 'jp1'
            me = watcher.summoner.by_name(my_region, summoner_name_data)
            my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])

            return render(request,'note/matchhistory_list.html',{'me': me, 'my_ranked_stats': my_ranked_stats,},)
        else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
            form = MyForm()
            return render(request, 'note/form.html', {'form': form,})

def matchhistory_list(request):
    watcher = RiotWatcher('RGAPI-e55e7d8d-2e50-4ea8-82f3-d5283c84b64d')
    my_region = 'jp1'
    me = watcher.summoner.by_name(my_region, 'アスペガイガー')
    my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])

    return render(request,'note/matchhistory_list.html',{'me': me, 'my_ranked_stats': my_ranked_stats,},)
