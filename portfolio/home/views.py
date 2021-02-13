from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method=='POST':
        print('This is POST')
        name=request.POST['fname']
        email=request.POST['email']
        phone=request.POST['phone']
        comment=request.POST['comment']
        print(f'{name} {email} {phone} {comment}')
        ins = Contact(name=name,email=email,phone=phone,comment=comment)
        ins.save()
        print('Data written to the database')
    return render(request, 'contact.html')