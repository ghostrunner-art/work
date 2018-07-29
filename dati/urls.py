from django.urls import path
from . import views

urlpatterns = [
    # 实际访问的地址是 localhost:8000/dati/
    path('',views.dati,name = 'dati_index'),

]