#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-12 2:47
# @Author  : qinzhifeng
# @FileName: helloworld.py
# @Software: PyCharm

'''
flask：本身就是一个web的一个内核，它是写 web 的一个框架，小巧，精简
django：比较大而杂，相当于一个精装房
目的：学习用 flask 去写接口（get，post），以及响应
一：请求  --- get,post  --- 默认的请求方式是 get，如果想用 post，需要去指定
二：响应  （1，3必须掌握）
1、json 数据   --- return jsonify()
2、文本
3、自己构造的响应
4、重定向302
'''

from flask import Flask, jsonify, request

# 实例化一个 app 对象，固定的代码
app = Flask(__name__)
# 通过路由装饰器写一个路由，固定代码，默认是get
# 指定 post 请求，通过 methods 关键字，methods=['get','POST']，指的是 get和post 两种方法都能用
@app.route('/', methods=['GET','POST'])
def helloword():
    '''
    helloword 是视图，视图名字不能重复
    :return:
    '''
    # return 指的是返回的响应值是什么类型及内容
    return 'helloword'

# 写一个返回 json 数据的接口
@app.route('/login', methods=['POST'])  # 路由，指定访问的url地址和请求方式
# def login 指，通过 route 路由访问后获取的资源内容
def login():
    # 前端页面传过来的数据，flask 是通过 request 这个参数来接收的（前端的参数都封装在 request 里面）
    # post 请求，通过 request.get_json()来获取数据，返回的数据就是字典的形式
    # 登录接口是我们自己定义的，比如 name 和 pwd
    # 1.获取前端传来的请求参数
    data = request.get_json()  # 定义请求参数为 json 格式
    # 2.参数校验
    if 'name' not in data or not data.get('name'):
        return jsonify({
            'code':404,
            'message':'invalid param name',
            'data':data
        })
    if 'pwd' not in data or not data.get('pwd'):
        return jsonify({
            'code':404,
            'message':'invalid param pwd',
            'data':data
        })
    name = data.get('name')     # 后台获取前端传来的用户名和密码
    pwd = data.get('pwd')
    # 3.处理参数
    try:
        print(name)
        print(pwd)
        print(data)
        # 4.返回响应
        return jsonify({
            'code':200,
            'message':'ok',
            'data':data
        })
    except Exception as e:
        return jsonify({
            'code': 200,
            'message': e,
            'data': data
        })

if __name__ == '__main__':
    '''
    debug=True 调试功能，可以自动加载更新的代码
    '''
    app.run(debug=True, port=5001)


