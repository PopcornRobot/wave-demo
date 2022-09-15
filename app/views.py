from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from app.models import Room

def index(request):
    return render(request, "app/index.html")

def room(request, room_name):
    print("----", room_name)
    username = request.GET.get('username', 'Anonymous')
    return render(request, 'app/room.html', {'room_name': room_name, 'username': username})

def room_detail(request, room_id):
    return render(request, 'app/room_detail.html', {'room_id': room_id})

def dashboard(request):
    return render(request, 'app/dashboard.html')

def dashboard_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'app/dashboard_rooms.html', {'rooms': rooms})

def create_room(request):
    room_name = request.POST['room_name']
    Room.objects.create(name=room_name)
    return HttpResponseRedirect('/dashboard')
    # return HttpResponse('create_room ' + room_name)