from django.shortcuts import render
from riotwatcher import RiotWatcher
from django.http import HttpResponse
from requests import HTTPError
import json
from django.template.loader import render_to_string
from .forms import MyForm
from .models import SNset
# Create your views here.


def form_test(request):
        if request.method == "GET":
            form = MyForm(request.GET)
        if form.is_valid():
            summoner_name_g = form.cleaned_data['Summonername']
            SNset_1 = SNset()#  ここでクラスを呼び出してインスタンスを生成
            ranked_dict = SNset_1.lol(summoner_name_g)#lolというメソッドをsummoner_name_gを引数として使用
            return render(request,'note/matchhistory_list.html',ranked_dict)
        else:
            form = MyForm()
            return render(request, 'note/form.html', {'form': form,})
def custom_404(request):
    return render(request, '404.html', {}, status=404)
