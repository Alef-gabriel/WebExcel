from django.http import HttpResponse
from django.shortcuts import render
from .form import UploadFileForm

def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST)
    
    form = UploadFileForm()
    return render(request, 'home/home.html', {'form':form})
