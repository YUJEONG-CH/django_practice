# URL 설정을 app단위로 !
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    # http://localhost:8000/articles
    path('', views.index, name='index'),
    # http://localhost:8000/articles/new
    # path('new/', views.new, name='new'),
    # http://localhost:8000/articles/create
    path('create/', views.create, name='create'),
    # http://localhost:8000/articles/1/ : 1번글
    # http://localhost:8000/articles/3/ : 3번글
    path('<int:pk>/', views.detail, name='detail'),
    # http://localhost:8000/articles/1/update/ : 1번글 수정
    # http://localhost:8000/articles/3/update/ : 3번글 수정
    path('<int:pk>/update/', views.update, name='update'),

]