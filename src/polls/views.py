import fsspec
from .calc import test
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render
from .form import UploadFileForm

#HttpResponseRedirect("http://127.0.0.1:8000/result/") if form.is_valid():
def index(request):
    form = UploadFileForm(request.POST)
    # if request.method == 'POST':
    #     file = request.FILES['fileXls']
    #     xls = test(file)     
    #     return FileResponse(request,xls)
    return render(request,'home/home.html',{'form':form})

def result(request):
    return FileResponse()
