from django.shortcuts import render, redirect
from datetime import datetime
from HMSapp.models import Contact
from HMSapp.models import Book
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def couple(request):
    return render(request,'coupleroom.html')

def family(request):
    return render(request,'familyroom.html')

def villa(request):
    return render(request,'villa.html')

def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        room = request.POST.get('room')
        guests = request.POST.get('guests')
        arrival = request.POST.get('arrival')
        departure = request.POST.get('departure')
        special = request.POST.get('req')
        book = Book(name=name, email=email, room=room, guests=guests, arrival=arrival, departure=departure, special=special)
        book.save()
        messages.success(request, 'Room Booked, You can pay for guaranteed reservation.')
    return render(request, 'login.html')

