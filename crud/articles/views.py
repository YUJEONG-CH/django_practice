from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# 요청 정보를 받아서...
def index(request):
    # 게시글을 가져와서..
    articles = Article.objects.order_by('-pk')# 역순 - queryset(Article객체를 가진)
    # Template에 전달한다..
    context = {
        'articles': articles
    }
    # 페이지를 render...
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # DB저장 로직
    title = request.GET.get('title')
    content = request.GET.get('content')
    Article.objects.create(title=title, content=content)
    return redirect('articles:index')