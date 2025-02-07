from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('data', views.data, name='data'),
    path('test', views.test, name='test')
]
