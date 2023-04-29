from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')
def main(request):
     return render(request,'main.html')
def teste(request):
    #return HttpResponse('oi')
    return render(request,'teste.html')
