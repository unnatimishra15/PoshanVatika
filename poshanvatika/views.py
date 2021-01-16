from django.shortcuts import render
from .forms import DocumentForm
from .models import DocumentModel
# Create your views here.

def home(request):

    return render(request,'nutrigarden.html')

def map(request):

    return render(request,'health.html')


def uploadDocument(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"File is saved.")
            return redirect('/article/')
    else:
        form = DocumentForm() # A empty, unbound form

    return render(request,'upload.html',{'form': form})

    return render(request,'upload.html')