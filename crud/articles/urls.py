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

]