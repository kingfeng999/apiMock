#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-12 5:23
# @Author  : qinzhifeng
# @FileName: flask_study.py
# @Software: PyCharm

from flask import Flask, request, make_response, redirect, url_for

''' 需求：
1、get 请求参数的获取
2、设置 cookie
3、自己构造响应：make_response()
4、跳转，redirect(url_for(函数的名字))
5、动态生成路由
'''

# 实例化一个 app 对象
app = Flask(__name__)

# 指定路由，动态生成
@app.route('/set/<name>')

# 设置 cookie 视图
def set_cookie(name):
    '''
    构造一个响应，在响应头里面添加 cookie
    :param name:
    :return:
    '''
    # 构造响应并跳转到另外一个视图，然后赋值给 resp 这个变量
    resp = make_response(redirect(url_for('hello')))
    # 给 resp 这个响应添加 cookie 值，方法是：set_cookie(键，值)
    resp.set_cookie('name', name)
    return resp

@app.route('/hello')
# 跳转 hello 视图
def hello():
    # 从请求里面获取参数，从 get 请求中获取参数用 request.args.get('name')
    name = request.args.get('name')
    # 对参数（动态路由传递的参数）进行验证
    # 如果动态路由传了 name 值，那么就直接返回响应，如果动态路由不传，那么就从 cookie 中获取
    if name is None:
        # 从 cookie 中获取 name 值，request.cookies.get() 获取请求头里面所有 cookie 的值
        name = request.cookies.get('name')
    return '<h1>hello：%s</h1>' %name


if __name__ == '__main__':
    '''
    debug=True 调试功能，可以自动加载更新的代码
    '''
    app.run(debug=True, port=5001)