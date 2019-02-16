from django.urls import path

from . import views

urlpatterns = [
    path('', views.tools, name='tools_index'),
    path('authorize/', views.authorize_user, name='authorize_user'),
    path('<int:tool_id>/', views.tool_page, name='tool'),
]
