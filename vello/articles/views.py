from django.shortcuts import render, get_object_or_404
from .models import VeloArticles
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def showarticles(request):
    first_article = VeloArticles.objects.get(id=1)
    artecles_velo = VeloArticles.objects.all()[1:]
    paginator = Paginator(artecles_velo, 4)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        artecles_velo = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        artecles_velo = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        artecles_velo = paginator.page(paginator.num_pages)
    return render(request, 'articles/articles.html', {'artecles_velo': artecles_velo, 'first_article':first_article})


def specific_article(request, article_id):
    article = VeloArticles.objects.get(id=article_id)
    return render(request, 'articles/specific_article.html', {'article': article})