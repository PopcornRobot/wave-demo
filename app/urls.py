from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room_name>/', views.room, name="room"),
    path('dashboard', views.dashboard),
    path('dashboard/rooms', views.dashboard_rooms),
    path('create_room', views.create_room),
]