from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    return render(request , 'main/index.html')
    
def corzina(request):
    return render(request , "main/korzi.html")

def carta(request):
    return render(request , "main/carta.html")

def logreg(request):
    return render(request , "main/logreg.html")



# у меня роутера нету я через раздачу
# нет
# он не может открыть а?