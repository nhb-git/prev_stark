#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/19/2020  7:32 PM 
# 文件名称   ：urls.py
from django.conf.urls import url
from app01 import views


urlpatterns = [
    url(r'login/', views.login),
    url(r'home/', views.home),
]
