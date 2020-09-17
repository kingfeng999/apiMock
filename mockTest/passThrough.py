#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-12 18:27
# @Author  : qinzhifeng
# @FileName: passThrough.py
# @Software: PyCharm
'''
实现透传的功能，保留原有接口的功能
原有接口的功能  http://127.0.0.1:5000/
/login
/register
'''
import requests
from flask import make_response


def passThrouth(data):
    '''
    判断条件：通过请求参数
    对登录的功能进行透传，保留原来的功能
    1、重新对原有的接口发起请求 --- 获取响应
    2、构造响应 make_response()
    3、把响应值返还回来
    :param data: 指的是前端收集到的请求参数
    :return:
    '''
    url = 'http://127.0.0.1:5000/login'
    # 模拟发起请求
    result = requests.post(url, json=data)
    # 构造响应，是把想返回的响应值放在 make_response 这个函数里面
    resp = make_response(result.json())
    return resp

def passThrouthRe(data):
    '''
    判断条件：通过请求参数
    对注册的功能进行透传，保留原来的功能
    1、重新对原有的接口发起请求 --- 获取响应
    2、构造响应 make_response()
    3、把响应值返还回来
    :param data: 指的是前端收集到的请求参数
    :return:
    '''
    url = 'http://127.0.0.1:5000/register'
    # 模拟发起请求
    result = requests.post(url, json=data)
    # 构造响应，是把想返回的响应值放在 make_response 这个函数里面
    resp = make_response(result.json())
    return resp


