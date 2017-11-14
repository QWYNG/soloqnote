from django import forms


class MyForm(forms.Form):
    Summonername = forms.CharField(max_length=100)
