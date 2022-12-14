from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from app.models import Room, Player

def index(request):
    return render(request, "app/index.html")

def room1(request, room_name):
    print("---- 1 ", room_name)
    username = request.GET.get('username', 'Anonymous')
    player = Player.objects.create(username="test")
    print("--- ", player)
    return render(request, 'app/room_1.html', {'room_name': room_name, 'username': username})

def room2(request, room_name):
    print("----", room_name)
    username = request.GET.get('username', 'Anonymous')
    player = Player.objects.create(username="test")

    return render(request, 'app/room_2.html', {'room_name': room_name, 'username': username})

def room3(request, room_name):
    print("----", room_name)
    username = request.GET.get('username', 'Anonymous')
    player = Player.objects.create(username="test")

    return render(request, 'app/room_3.html', {'room_name': room_name, 'username': username})

def room4(request, room_name):
    print("----", room_name)
    username = request.GET.get('username', 'Anonymous')
    player = Player.objects.create(username="test")

    return render(request, 'app/room_4.html', {'room_name': room_name, 'username': username})



def room_detail(request, room_id):
    return render(request, 'app/room_detail.html', {'room_id': room_id})

def dashboard(request):
    room_count = Room.objects.all().count()
    return render(request, 'app/dashboard.html', {'room_count': room_count})

def dashboard_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'app/dashboard_rooms.html', {'rooms': rooms})

def create_room(request):
    room_name = request.POST['room_name']
    Room.objects.create(name=room_name)
    return HttpResponseRedirect('/room/' + room_name + '/?username=user')
    # return HttpResponseRedirect('/dashboard/rooms')
    # return HttpResponse('create_room ' + room_name)