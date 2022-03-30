from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

nextId = 5
topics = [
    {'id': 1, 'title': 'Netflix', 'body': 'Netflix is ...'},
    {'id': 2, 'title': 'Wavve', 'body': 'Wavve is ...'},
    {'id': 3, 'title': 'Tving', 'body': 'Tving is ...'},
    {'id': 4, 'title': 'ApplePlay', 'body': 'ApplePlay is ...'}
]


def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = f'''
                <li>
                    <form action="/delete/" method="post">
                        <input type="hidden" name= "id" value={id}>
                        <input type="submit" value="delete">
                    </form>
                </li>
                <li><a href="/update/{id}">update</a></li>
                ''' if id else ''
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(f'''
        <html>
        <body>
            <h1><a href='/'>OTT Platform</a><h1/>
            <ol>
                {ol}
            </ol>
            {articleTag}
            <ul>
                <li><a href='/create'>create</a></li>
                {contextUI}
            </ul>
        </body>
        </html>
        ''')


def index(request):
    article = """
    <h2>Welcome</h2>
    Hello, Ott
    """
    return HttpResponse(HTMLTemplate(article))


def read(request, id):
    global topics
    articles = [f'<h2>{topic["title"]}</h2>{topic["body"]}'for topic in topics if topic["id"] == int(id)]
    return HttpResponse(HTMLTemplate(articles[0], id))


@csrf_exempt
def update(request, id):
    global topics
    selected_topic = [topic for topic in topics if topic["id"] == int(id)][0]
    if request.method == 'GET':
        article = f'''
            <form action="/update/{id}" method="post">
                <p><input type="text" name="title" placeholder="title" value="{selected_topic["title"]}"></p>
                <p><textarea name="body" placeholder="body">{selected_topic["body"]}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
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
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST["title"]
        body = request.POST["body"]
        new_topic = {"id": nextId, "title": title, "body": body}
        topics.append(new_topic)
        url = '/read/' + str(nextId)
        nextId += 1
        return redirect(url)



