from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    # Make this the last, so the url pattern will be checked last
    path('<str:slug>/', views.article_detail, name='detail')
]
