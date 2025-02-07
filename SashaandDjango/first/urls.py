from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('data', views.data, name='data'),
    path('test', views.test, name='test')
]
