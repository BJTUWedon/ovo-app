#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/10/13 19:56
# @Author : 吴宇栋
# @Site : 
# @File : base64.py
# @Software: PyCharm

from django.shortcuts import render,HttpResponse
import time


def add_face_data(request):
        time.sleep(5)
        key = request.POST.get('imgurl')
        key = str(key)
        print(key[23:])
