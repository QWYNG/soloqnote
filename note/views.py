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
            watcher = RiotWatcher('RGAPI-55c1d19e-bbe9-4eb0-99c0-207875f6fef7')
            my_region = 'jp1'
            me = watcher.summoner.by_name(my_region, summoner_name_data)
            spectator = watcher.spectator.by_summoner(my_region, me['id'])

            return render(request,'note/matchhistory_list.html',{'me': me, 'spectator': spectator,},)
        else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
            form = MyForm()
            return render(request, 'note/form.html', {'form': form,})
