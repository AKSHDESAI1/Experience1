from django.shortcuts import render

from expapp.models import uploadDocument

# Create your views here.
def upload(request):
    if request.method == 'POST':
        print(request.FILES['file'])
        doc = uploadDocument(files=request.FILES['file'])
        doc.save()
    return render(request,'upload.html')