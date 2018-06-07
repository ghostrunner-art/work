# -*- coding: utf-8 -*-

from django.urls import path
from . import views
urlpatterns = [
    #path('shuchu/',views.shuchu,name = 'shuchu'),
    # localhost:8000/article/
    path('',views.article_list,name='article_list'),
    # localhost:8000/article/2
    # 该路径从总路由过来，均为article路径下内容
    path('<int:article_id>',views.article_detail,name='chedan'),

]