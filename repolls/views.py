from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('It is index')

def read(request, id):
    print(id)
    return HttpResponse('''
    <h1>Django</h1>
    <ol>
        <li>Html</li>
        <li>css</li>
        <li>javascript</li>
    </ol>
    ''')

def randoms(request):
    return HttpResponse(str(random.random()))
    # return HttpResponse('hello')