from django.conf.urls import url
from food_waste_management_app import views

urlpatterns =[
    url(r'^$', views.index, name='index'), #access the view called index
    ]
