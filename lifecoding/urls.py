from django.urls import path
from . import views

app_name="lifecoding"

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('read/<int:id>/', views.read, name='read'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    ] 