from multiprocessing import context
from django.shortcuts import render

from django.views import View
import requests


# Create your views here.

class HelloWorldView(View):
    def get(self, request, name='world'):
        context = {'name': name}
        return render(request=request, template_name='hello_world.html', context= context)



class HelloNameView(View):
    def get(self, request, name):
        context = { 'name':name}
        return render(request=request, template_name='hello_name.html', context=context)
    
class GoodbyeView(View):
    def get(self, request, name):
        context = {'name' : name}
        return render(request, 'goodbye.html', context)
    
class CryptoStatsView(View):
    def get(self, request):
        api_key = 'YOUR API KEY'
        api_url = f'https://cloud.iexapis.com/stable/crypto/{symbol}/price?token={api_key}'
        raw = requests.get(api_url).json()
        context = {'price': raw['price']}
        return render(request, crypto.html, context)