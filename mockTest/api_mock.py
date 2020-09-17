#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-12 6:16
# @Author  : qinzhifeng
# @FileName: api_mock.py
# @Software: PyCharm
'''
mock 档板
作用：其实保证你的测试业务可以顺利的进行，保证业务流程通畅且稳定
mock 使用场景：
1、调用第三方接口，为了让流程走通
2、功能没有开发完成，如：登录接口被锁定，已经补加入黑名单
需求：
癸未接口没有黑名单这个功能
todo 1.做一个 mock 服务（档板），实现黑名单功能
todo 2.这个登录接口原有的功能需要保留（登录成功...）  --- 透传
'''

from flask import Flask,jsonify,request
from mockTest.passThrough import passThrouth,passThrouthRe

# 实例化一个 app 对象
app = Flask(__name__)
# 响应里面识别中文，如下更改：
app.config['JSON_AS_ASCII'] = False
# 添加登录路由，实现 mock 功能
@app.route('/login/mock', methods=['POST'])
def login():
    '''
    实现黑名单的功能
    :return:
    '''
    data = request.get_json()
    name = data.get('name')
    if name == '黑名单':
        return jsonify({
            'data':data,
            'message':'您已经被我们公司加入黑名单',
            'code':200
        })
    else:
        # 不走黑名单这个 mock 服务，想走原来的功能（登录）
        resp = passThrouth(data)
        return resp

# 实现透传注册的功能，动态生成路由，注册的 url 最好跟之前服务的 url 一样
@app.route('/<func>', methods=['POST'])
def register(func):
    # 判断条件：前端传进来的参数
    data = request.get_json()
    if func == 'register':
        # 透传注册功能
        resp = passThrouthRe(data)
        return resp

# 启动服务
if __name__ == '__main__':
    app.run(dabug=True, port=9999)

