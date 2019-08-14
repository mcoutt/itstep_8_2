from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'page1.html', {})


def webexample(request):
    return render(request, 'page.html', {})
