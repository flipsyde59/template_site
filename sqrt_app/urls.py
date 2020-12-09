from django.urls import path

from . import views

app_name = 'sqrt_app'

urlpatterns = [
    path('', views.index, name='index'),
    #path('/getSqrt', views.get_sqrt, name='get_sqrt')
]