from django.shortcuts import render

def home(request):
    context = {
    'title': 'Home',
    'description': '',
    'keywords': '',
    }
    return render(request, 'main_page/home.html', context)
