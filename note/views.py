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
            watcher = RiotWatcher('RGAPI-ee54c73d-6709-4623-bd24-42346712bb4d')
            my_region = 'jp1'
            me = watcher.summoner.by_name(my_region, summoner_name_data)
            my_ranked_stats  = watcher.league.positions_by_summoner(my_region, me['id'])
            dict = {'my_ranked_stats': my_ranked_stats, 'me': me}
            return render(request,'note/matchhistory_list.html',dict,)
        else:
            form = MyForm()
            return render(request, 'note/form.html', {'form': form,})
def custom_404(request):
    return render(request, '404.html', {}, status=404)
