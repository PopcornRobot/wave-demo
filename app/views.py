from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, "app/index.html")

def room (request, room_name):
    print("----", room_name)
    username = request.GET.get('username', 'Anonymous')
    return render(request, 'app/room.html', {'room_name': room_name, 'username': username})

def dashboard(request):
    return render(request, 'app/dashboard.html')

def dashboard_rooms(request):
    return render(request, 'app/dashboard_rooms.html')
    
def create_room(request):
    room_name = request.POST['room_name']
    return HttpResponseRedirect('/dashboard')
    # return HttpResponse('create_room ' + room_name)