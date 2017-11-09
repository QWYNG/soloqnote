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
            summoner_name_data = form.cleaned_data['text']
            watcher = RiotWatcher('RGAPI-434613a8-af64-4d55-92bb-413233e233f3')
            my_region = 'jp1'
            me = watcher.summoner.by_name(my_region, summoner_name_data)
            my_ranked_stats  = watcher.league.positions_by_summoner(my_region, me['id'])

            return render(request,'note/matchhistory_list.html',{'me': me, 'my_ranked_stats': my_ranked_stats,},)
        else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
            form = MyForm()
            return render(request, 'note/form.html', {'form': form,})
