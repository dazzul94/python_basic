from django.urls import path

from . import views

app_name = 'pets'

urlpatterns = [
    path('', views.pet_form, name='pet_form'), # ex: /pets/
    path('results', views.results, name='results'), # ex: /pets/
]