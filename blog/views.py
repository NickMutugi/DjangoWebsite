from django.shortcuts import render
from .models import Contact, Contact1

def homepage(request):
    return render (request, 'blog/homepage.html')


def contact(request):
    if request.method=='POST':
        names=request.POST.get('name')
        emails=request.POST.get('email')
        messages=request.POST.get('message')
        c=Contact(name=names,email=emails,message=messages)
        c.save()
        return render(request,'blog/thankyou.html')
    else:
        return render(request,'blog/contact.html')

def thankyou(request):
    if request.method=='POST':
        name3=request.POST.get('name2')
        email3=request.POST.get('email2')
        message3=request.POST.get('message2')
        d=Contact1(name1=name3,email1=email3,message1=message3)
        d.save()
        return render(request,'blog/thank.html')
