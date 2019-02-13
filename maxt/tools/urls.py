from django.urls import path

from . import views

urlpatterns = [
    path('', views.tools, name='tools_index'),
    path('<int:tool_id>/', views.tool_page, name='tool'),
]
