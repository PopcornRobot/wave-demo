from django.urls import path

from . import views
app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room_name>/', views.room1, name="room1"),
    path('room2/<str:room_name>/', views.room2, name="room2"),
    path('room3/<str:room_name>/', views.room3, name="room3"),
    path('room4/<str:room_name>/', views.room4, name="room4"),
    path('dashboard', views.dashboard),
    path('dashboard/rooms', views.dashboard_rooms),
    path('dashboard/rooms/<int:room_id>', views.room_detail, name="room_detail"),
    path('create_room', views.create_room),
]