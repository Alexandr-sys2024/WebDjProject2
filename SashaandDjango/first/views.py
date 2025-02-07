from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')



def data(request):
    return HttpResponse("Hello, this is the data view!")


def test(request):
    return HttpResponse("Hello, this is the test view!")

