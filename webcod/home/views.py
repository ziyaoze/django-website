
from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home/site.html')
def about(request):
    return render(request, 'home/about.html')
def contact(request):
    
    if request.method=='POST':
        namedata=request.POST['name']
        emaildata=request.POST['email']
        contentdata=request.POST['content']
        if len(namedata)<2 or len(emaildata)<8 or len(contentdata)<1:
            messages.error(request, 'please enter form correctly')
        else:
            contactdata=Contact(name=namedata,content=contentdata,email=emaildata)
            contactdata.save()
            messages.success(request, 'form submitted succesfully')

        
    return render(request, 'home/contact.html')
