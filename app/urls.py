from django.urls import path

from . import views
app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<str:room_name>/', views.room, name="room"),
    path('dashboard', views.dashboard),
    path('dashboard/rooms', views.dashboard_rooms),
    path('dashboard/rooms/<int:room_id>', views.room_detail, name="room_detail"),
    path('create_room', views.create_room),
]