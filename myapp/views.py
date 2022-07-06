from django.shortcuts import render, HttpResponse

# Create your views here.

topics =[
{'id':1, 'title':'routing', 'body':'Routing is...'},
{'id':2, 'title':'view', 'body':'view is...'},
{'id':3, 'title':'model', 'body':'model is...'},
]

def HTMLTemplate(articletag):
    global topics
    #이걸 어떻게 해석해야할까?
    ol = ''
    '''
        python
            None + str
            str + str
            ol = '' # 강제로 ol을 str
            1. 초기값이 있어야 += 
            2. str + str 형식 유지
    '''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href='/'>Django</a></h1>
        <ol>
            {ol}
        </ol>
         {articletag} 
    </body>
    </html>
    '''


def index(request):
    article ='''
    <h2>Welcome</h2>
    Hello, Django 
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article =''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse('create!')






