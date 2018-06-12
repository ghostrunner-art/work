from django.urls import path
from . import views

urlpatterns = [
    # 实际访问的地址是 localhost:8000/blog/
    path('',views.blog_list,name = 'blog_list'),
    path('<int:blog_pk>',views.bolg_detail,name='blog_detail'),
    path('type/<int:blog_type_pk>',views.blogs_with_type,name = 'blogs_with_type'),
]