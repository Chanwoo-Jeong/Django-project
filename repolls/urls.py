from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('read/<id>/', views.read, name='read'),
    path('randoms',views.randoms, name='randoms')
]