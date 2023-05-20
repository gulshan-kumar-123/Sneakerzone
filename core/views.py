from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def wishlist(request):
    return render(request, 'core/wishlist.html')

def cart(request):
    return render(request, 'core/cart.html')

def login(request):
    return render(request, 'core/login.html')

def signup(request):
    return render(request, 'core/signup.html')

def browse(request):
    return render(request, 'core/browse.html')

def search(request):
    return render(request, 'core/search.html')

