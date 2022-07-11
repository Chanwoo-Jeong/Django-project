from django.shortcuts import render, HttpResponse , get_object_or_404
import random
from repolls.models import Question

# Create your views here.
def index(request):
    latest_question_list =  Question.objects.all().order_by('pub_date')[:5]
    return  render(request, 'repolls/index.html', {'latest_question_list':latest_question_list} )

def read(request, id):
    print(id)
    return HttpResponse(f'''
    <h1>Django</h1>
    <ol>
        <li>Html</li>
        <li>css</li>
        <li>javascript</li>
    </ol>
    {id}
    ''')

def randoms(request):
    return HttpResponse(str(random.random()))
    # return HttpResponse('hello')

def detail(request,question_id):
    question =  get_object_or_404(Question,pk=question_id)
    return render(request, 'repolls/detail.html' , {'question':question})

def results(request,question_id):
    return HttpResponse('''
    its result page
    ''')

def vote(request,question_id):
    return HttpResponse('''
    its vote page
    ''')