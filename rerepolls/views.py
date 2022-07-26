from django.shortcuts import render , HttpResponse , get_object_or_404 , render 
from rerepolls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    question_list = Question.objects.all().order_by('-pub_date')[:5]
    return render(request, 'rerepolls/index.html',{'question':question_list}) 

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'rerepolls/detail.html', {'question':question})

def votes(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST.get('choice'))
        # Choice.objects.filter(question_id = question.pk).get()
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'rerepolls/detail.html',{
                'question': question ,
                'error_message': "You didn't select a choice.",
            })
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('rerepolls:results', args=(question_id,)))
    # selected_choice = question.choice_set.get(pk=request.POST['choice'])
    

    # selected_choice.votes += 1 
    # selected_choice.save()

    # return HttpResponseRedirect(reverse('rerepolls:results', args=(question_id,)))

def results(request, question_id):
    return render (request, 'rerepolls/results.html')
