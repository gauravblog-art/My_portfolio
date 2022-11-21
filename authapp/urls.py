
from django.urls import path
from authapp import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.handlogin, name='handlogin'),
    path('logout/', views.handlogout, name='handlogout'),

]
