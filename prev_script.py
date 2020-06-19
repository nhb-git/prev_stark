#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/19/2020  8:56 PM 
# 文件名称   ：prev_script.py
from django.conf.urls import url
from app01 import views


class StarkSite:
    """
    程序启动时的预加载组件
    """
    def __init__(self):
        self._apps = []

    def register_app(self, app_name):
        """
        注册app名称到列表中
        :param app_name:
        :return:
        """
        self._apps.append(app_name)

    def get_url(self):
        patterns = []
        for app in self._apps:
            patterns.append(url(r'^%s' % app, views.login))
        return patterns

    @property
    def urls(self):
        """
        路由信息
        :return:
        """
        return self.get_url(), None, None


site = StarkSite()
