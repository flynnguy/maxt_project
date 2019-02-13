from django.urls import path

from . import views

urlpatterns = [
    path('<slug:username>/', views.userinfo, name='userinfo'),
    path('rfid.csv', views.rfid_csv, name='rfid'),
]
