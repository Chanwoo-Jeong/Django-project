from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Dictionary
from django.views.decorators.csrf import csrf_exempt

def index(request):
    dictionary_list = Dictionary.objects.all()
    return render(request, 'index.html',{'diclist': dictionary_list})

@csrf_exempt
def create(request):
    dictionary_list = Dictionary.objects.all()
    print("request.method",request.method)
    print("request.path",request.path)
    if request.method == "GET":
        create

    return render(request,'index.html',{'diclist':dictionary_list})

def read(request,id):
    dictionary_list = Dictionary.objects.all()
    dicpa_list = get_object_or_404(Dictionary, pk=id)
    return render(request,'index.html',{'diclist':dictionary_list,'dicpa':dicpa_list})

def update(request):
    return HttpResponse("im update")

def delete(request):
    return HttpResponse("im delete")
# Create your views here.
