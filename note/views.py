from django.shortcuts import render
from riotwatcher import RiotWatcher
from django.http import HttpResponse
from requests import HTTPError
from .forms import MyForm
from .models import Summoner
# Create your views here.


def summoner_name_form(request):
    if request.method == "GET":
        form = MyForm(request.GET)
    if form.is_valid():
        summoner_name = form.cleaned_data['Summonername']
        summoner = Summoner()
        ranked_dict = summoner.get_match_data(summoner_name)
        return render(request, 'note/matchhistory_list.html', ranked_dict)
    else:
        form = MyForm()
        return render(request, 'note/form.html', {'form': form, })
