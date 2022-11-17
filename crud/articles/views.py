from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

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

# def new(request):
#     article_form = ArticleForm()
#     context = {
#         'article_form': article_form
#     }
#     return render(request, 'articles/new.html', context=context)

def create(request):
    if request.method == 'POST':
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)


    