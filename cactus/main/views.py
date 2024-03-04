from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request , 'main/index.html')
    
def about(request):
    return HttpResponse('About page')

# у меня роутера нету я через раздачу
# нет
# он не может открыть а?