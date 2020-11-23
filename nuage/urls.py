from django.urls import path, include
from . views import *
urlpatterns = [
    path('<int:id>/',
         GenericApiView.as_view(), name='int_api'),
    path('',
         GenericApiView.as_view(), name='generic_api'),
    path('create_user/',
         GenericUserApiView.as_view(), name='user_api'),


]
