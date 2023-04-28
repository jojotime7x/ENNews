from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.fetch_news, name='fetch_news'),
    path('search/', views.search_news, name='search_news'),
    path('add_favorite/', views.add_favorite, name='add_favorite'),
    path('delete_favorite/<int:article_id>/', views.delete_favorite, name='delete_favorite'),
]
