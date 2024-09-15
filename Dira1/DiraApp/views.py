from django.shortcuts import render

def home_dira(request):
    return render(request, 'index.html')
