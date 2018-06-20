from django.urls import path
from . import views

urlpatterns = [
    # 实际访问的地址是 localhost:8000/blog/
    path('',views.blog_list,name = 'blog_list'),
    path('<int:blog_pk>',views.bolg_detail,name='blog_detail'),
<<<<<<< HEAD
    path('type/<int:blog_type_pk>',views.blogs_with_type,name='blogs_with_type'),
    path('date/<int:year>/<int:month>',views.blogs_with_date,name='blogs_with_date'),
=======
    path('type/<int:blog_type_pk>',views.blogs_with_type,name = 'blogs_with_type'),
    path('date/<int:year>/<int:month>',views.blogs_with_date,name='blogs_with_date')
>>>>>>> cd57c9b30df5dbf4e04eb557a075b48d11795c88
]