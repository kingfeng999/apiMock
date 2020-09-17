#!/usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-16 2:36
# @Author  : qinzhifeng
# @FileName: jisuan.py
# @Software: PyCharm

a = ['h','e','l','l','o']
print(''.join(a))
s = ''
for item in a:
    s += item
print(s)


for i in range(1,10):
    for j in range(1, i+1):
        print('{}*{}={}\t'.format(j, i, j*i), end='')
    print()

str = [23,78,90,46,9,5,288,356,1,76]
for i in range(len(str)):
    for j in range(len(str) - i - 1):
        if str[j] < str[j+1]:
            # str[j+1],str[j] = str[j],str[j+1]
            str[j],str[j+1] = str[j+1],str[j]
print(str)

num = [10,30,50]
sum = 0
for i in range(len(num)):
    sum += num[i]
print(sum)

sum = 0
for i in range(101):
    if i % 2 == 1:
        sum += i
print(sum)


# aa = ['r','a','s']
aa = [33,10,56]
# aa.sort(reverse=True)
aa.reverse()
print(aa)

print("我叫 %s,今年 %d 岁了" %('小明',10))
name = '小明'
print(f"我的名字叫：{name}")

a = 'a:b:c:d:e'
a = a.replace(':','--')
print(a)

a = 'abcddeegg'
a = a.split('c',',')
print(a)


txt = "Google#Runoob#Taobao#Facebook"
# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)

print(x)