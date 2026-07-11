from django.urls import path
from . import views
urlpatterns=[
    path('login/',views.log_in,name='login'),
    path('',views.sign_up,name='signup'),
    path('create/',views.create,name='create'),
    path('home/',views.home,name='home'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('toggle/<int:pk>/',views.toggle,name='toggle'),
    path('logout/',views.log_out,name='logout')
]