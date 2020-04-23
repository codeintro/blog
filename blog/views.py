from django.shortcuts import render, redirect
from .models import Post, User


def register(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        if username and password:
            User.objects.create(username=username, password=password).save()
            return redirect('/login')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = User.objects.filter(username=username, password=password).first()
        request.session['is_login'] = True
        request.session['user_id'] = user_obj.id
        request.session['username'] = user_obj.username
        if user_obj:
            return redirect('/index')
        else:
            return redirect('/login')
    return render(request, 'login.html')


def logout(request):
    request.session.flush()
    return redirect('/login')


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        if title and body and request.session['is_login']:
            Post.objects.create(title=title, body=body, author_id_id=request.session['user_id']).save()
            return redirect('/index')
    return render(request, 'create.html')


def index(request):
    articles = Post.objects.all()
    context = {'articles': articles}
    return render(request, 'index.html', context)
