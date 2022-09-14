from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def room (request, room_name):
    print("----", room_name)
    username = request.GET.get('username', 'Anonymous')
    return render(request, 'app/room.html', {'room_name': room_name, 'username': username})