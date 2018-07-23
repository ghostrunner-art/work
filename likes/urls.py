from django.urls import path
from . import views

urlpatterns=[
    path('like_chang',views.like_change,name='like_change')
]