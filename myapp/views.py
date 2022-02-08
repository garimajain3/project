from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'myapp/index.html')

def about(request):
    return render(request , 'myapp/contact.html')

def rooms(request):
    return render(request , 'myapp/rooms.html')

def dives(request):
    return render(request , 'myapp/dives.html')

def food(request):
    return render(request , 'myapp/foods.html')

def news(request):
    return render(request , 'myapp/news.html')

def contact(request):
    return render(request , 'myapp/contact.html')

