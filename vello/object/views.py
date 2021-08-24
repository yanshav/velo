from django.shortcuts import render
from .models import VeloObject
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def showobject(request):

    object_marsh = VeloObject.objects.all()
    paginator = Paginator(object_marsh, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        object_marsh = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        object_marsh = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        object_marsh = paginator.page(paginator.num_pages)
    return render(request, 'object/objects.html', {'object_marsh': object_marsh})

def specific_object(request, object_id):
    object = VeloObject.objects.get(id=object_id)
    return render(request, 'object/specific_object.html', {'object': object})
