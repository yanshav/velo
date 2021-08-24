from django.shortcuts import render

# Create your views here.

def navigator(request):
	return render(request, 'navigator/navigator.html')