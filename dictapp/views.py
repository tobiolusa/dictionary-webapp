from pydoc import source_synopsis
from django.shortcuts import render
from django.http import request
import requests
from bs4 import BeautifulSoup

# Create your views here.


def home(request):
    if request.method == "POST":
        word = request.POST['word']
        url = 'https://www.dictionary.com/browse/'+word
        r = requests.get(url)
        data = r.content
        soup = BeautifulSoup(data, 'html.parser')
        span = soup.find_all('span', {"class": "one-click-content"})
        dv = soup.find_all('div', {"class": "one-click-content css-10kvu73 e12fnee30"})


        param = {'text': span[0].text, 'word': word}
        return render(request, 'home.html', param)
    else:
        return render(request, 'home.html')