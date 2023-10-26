from django.urls import path
from InstaUser import views

urlpatterns = [
    path('', views.SignIn,  name='signin'),
]
