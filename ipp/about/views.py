from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>O nas</h1>')