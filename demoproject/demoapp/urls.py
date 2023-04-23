from django.urls import path
from . import views
urlpatterns = [

    path('my_view/',views.my_view,name='my_view'),

    path('',views.login,name='login_page'),
    path('home/',views.home,name='home_page'),
]