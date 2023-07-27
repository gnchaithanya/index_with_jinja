from django.urls import path
from app.views import *
app_name='something'
urlpatterns=[
    path('index/',index,name='index')
]