from django.urls import path

from real_estate import views

app_name = 'real_estate'

urlpatterns = [
    path('', views.home, name="main_home"),
    path('one_property/<uuid:uuid_property>/', views.get_single_property, name="one_property"),

]
