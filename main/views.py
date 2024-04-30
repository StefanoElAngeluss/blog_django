from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html', {
        'title': 'Á propos',})

def contact(request):
    return render(request, 'blog/contact.html', {
        'title': 'Contact',
    })