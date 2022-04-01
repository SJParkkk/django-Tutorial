from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.views.decorators.csrf import csrf_exempt

nextId = 5
topics = [
    {'id': 1, 'title': 'Netflix', 'body': 'Netflix is ...'},
    {'id': 2, 'title': 'Wavve', 'body': 'Wavve is ...'},
    {'id': 3, 'title': 'Tving', 'body': 'Tving is ...'},
    {'id': 4, 'title': 'ApplePlay', 'body': 'ApplePlay is ...'}
]


def index(request):
    context = {
        'article': {'title': 'Welcome', 'body': 'Hello, ott'},
        'topics': topics
    }
    return render(request, 'home.html', context)


def read(request, id):
    global topics
    selected_title = None
    selected_body = None
    for topic in topics:
        if topic["id"] == int(id):
            selected_title, selected_body = topic["title"], topic["body"]
    context = {
        'article': {'title': selected_title, 'body': selected_body},
        'topics': topics,
        'id': id
    }
    return render(request, 'home.html', context)


@csrf_exempt
def update(request, id):
    global topics
    selected_title = None
    selected_body = None
    for topic in topics:
        if topic["id"] == int(id):
            selected_title, selected_body = topic["title"], topic["body"]
    if request.method == 'GET':
        context = {
            'article': {'title': selected_title, 'body': selected_body},
            'topics': topics,
            'id': id
        }
        return render(request, 'home.html', context)
    elif request.method == 'POST':
        title = request.POST["title"]
        body = request.POST["body"]
        for topic in topics:
            if topic["id"] == int(id):
                topic["title"] = title
                topic["body"] = body
        return redirect(f'/read/{id}')


@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        topics = [topic for topic in topics if topic["id"] != int(id)]
        return redirect('/')


@csrf_exempt
def create(request):
    global nextId
    if request.method == 'POST':
        title = request.POST["title"]
        body = request.POST["body"]
        new_topic = {"id": nextId, "title": title, "body": body}
        topics.append(new_topic)
        url = '/read/' + str(nextId)
        nextId += 1
        return redirect(url)




