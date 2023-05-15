from django.shortcuts import render
from .models import Projects, Contact, About, IndexImage
from django.http.response import FileResponse 
# Create your views here.
def home(request):
    projects = Projects.objects.all().order_by('-id')
    homeimage = IndexImage.objects.all().order_by('-id')
    context = {
        'projects':projects,
        'homeimage': homeimage,
    }
    return render(request, 'index.html', context)


def download(request):
    obj = About.objects.get(id=1)
    filename = obj.cv.path
    response = FileResponse(open(filename, 'rb'))
    return response 
    

def func_404(request, exception):
    return render(request, '404.html')

