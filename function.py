#!/usr/bin/python
#coding=utf-8

def area(width, height = 6):
  return width * height

def print_hello(name):
  print 'hi, ' + name

print_hello('kyChu');

w, h = 4, 5
print("width = %d, height = %d, area = %d" %(w, h, area(w, h)))
print ("default height : area = %d" %(area(w)))
####匿名函数
sum = lambda arg1, arg2: arg1 + arg2;
print "w + h = ", sum(w, h);

total = 0;
def sum(arg1, arg2):
  #声明使用全局 使用 global 关键字 修饰
  #修改嵌套作用域 使用 nonlocal 关键字 修饰
  #内部使用外部变量时 为只读权限
  total = arg1 + arg2;
  print "函数内局部变量: ", total
  return total;

sum(10, 20);
print "函数外全局变量: ", total

