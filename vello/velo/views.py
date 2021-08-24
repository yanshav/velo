from django.shortcuts import render, get_object_or_404
from .models import VeloMarsh, Marsh,Quetion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.
def showmain(request):
    marhs = VeloMarsh.objects
    quetion = Quetion.objects
    return render(request, 'velo/main.html', {'marhs': marhs,'quetion': quetion})

def navigator(request):
    return render(request, 'velo/navigator.html')
@login_required
def saved(request):
    return render(request, 'velo/saved.html')

# Create your views here.
def showoMarsh(request, marsh_id):
    item_marsh = Marsh.objects.filter(name__id=marsh_id)
    marshs = VeloMarsh.objects.all()
    marsh = VeloMarsh.objects.get(id=marsh_id)
    paginator = Paginator(item_marsh, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        item_marsh = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        item_marsh = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        item_marsh = paginator.page(paginator.num_pages)
    return render(request, 'velo/route.html', {'item_marsh': item_marsh, 'marsh':marsh, 'marshs':marshs})

def showowartorymarsh(request, marsh_id):
    war_marsh = Marsh.objects.all()
    marsh = VeloMarsh.objects.get(id=marsh_id)
    paginator = Paginator(war_marsh, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        war_marsh = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        war_marsh = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        item_marsh = paginator.page(paginator.num_pages)
    return render(request, 'velo/route.html', {'war_marsh': war_marsh, 'marsh':marsh})

