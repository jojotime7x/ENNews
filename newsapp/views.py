import requests
from django.shortcuts import render, redirect
from .models import FavoriteArticle


def fetch_news(request):
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=6686d39b398a4b5796aeb26cee49c40d'  # Replace with your desired API endpoint
    params = {
        'country': 'us',
        'apiKey': '6686d39b398a4b5796aeb26cee49c40d',  # Replace with your actual API key
    }

    response = requests.get(url, params=params)
    news_data = response.json().get('articles', [])

    context = {
        'news_data': news_data,
    }
    return render(request, 'newsapp/news.html', context)

def search_news(request):
    search_query = request.GET.get('query', '')

    # Fetch news articles from the API based on the search query
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=6686d39b398a4b5796aeb26cee49c40d'  # Replace with your desired API endpoint
    params = {
        'q': search_query,
        'apiKey': '6686d39b398a4b5796aeb26cee49c40d',  # Replace with your actual API key
    }

    response = requests.get(url, params=params)
    news_data = response.json().get('articles', [])

    # Get favorite articles
    favorite_articles = FavoriteArticle.objects.all()

    context = {
        'news_data': news_data,
        'favorite_articles': favorite_articles,
    }
    return render(request, 'newsapp/search.html', context)

def add_favorite(request):
    title = request.POST.get('title', '')
    description = request.POST.get('description', '')
    url = request.POST.get('url', '')
    url_to_image = request.POST.get('url_to_image', '')

    article = FavoriteArticle(title=title, description=description, url=url, url_to_image=url_to_image)
    article.save()

    return redirect('search_news')

def delete_favorite(request, article_id):
    article = FavoriteArticle.objects.get(pk=article_id)
    article.delete()

    return redirect('search_news')
