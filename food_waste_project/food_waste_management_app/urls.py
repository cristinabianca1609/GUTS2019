from django.conf.urls import url
from food_waste_management_app import views

#Template urls
app_name = 'food_waste_management_app'

urlpatterns =[
    url(r'^$', views.index, name='index'), #access the view called index
    url(r'^register/', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    url(r'^food_monitor/$', views.food_monitor, name='food_monitor'),
    url(r'^capture/$', views.capture, name='capture'),
    # url(r'^foo/$', views.foo, name='foo'),
    url(r'^add_user_product/$', views.add_user_product, name='add_user_product'),
    url(r'^list_user_products/$', views.list_user_products, name='list_user_products'),
    url(r'^download.ics$', views.download_ics, name='download_ics'),
    ]
