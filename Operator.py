#!/usr/bin/python
# -*- coding: UTF-8 -*-

print '----------- test 1 -----------'#算术运算符
# +	加法
# -	减法
# ×     乘法
# /     除法（与类型有关）
# %     取模
# **    求幂
# //    整除

a = 21
b = 10
c = 0

c = a + b
print "1, c = ", c

c = a - b
print "2, c = ", c 

c = a * b
print "3, c = ", c 

c = a / b
print "4, c = ", c 

c = a % b
print "5, c = ", c

a = 2
b = 3
c = a**b 
print "6, c = ", c

a = 10
b = 5
c = a//b 
print "7, c = ", c

print '----------- test 2 -----------'#比较运算符
# ==     判断相等         False/true
# !=     判断不等         False/true
# <>     判断不等         同  !=
# >      判断大于         False/true
# <      判断小于         False/true
# >=     大于等于         False/true
# <=     小于等于         False/true

a = 21
b = 10
c = 0

if ( a == b ):
   print "1, a == b"
else:
   print "1, a != b"

if ( a != b ):
   print "2, a != b"
else:
   print "2, a == b"

if ( a <> b ):
   print "3, a != b"
else:
   print "3, a == b"

if ( a < b ):
   print "4, a < b" 
else:
   print "4, a >= b"

if ( a > b ):
   print "5, a > b"
else:
   print "5, a <= b"

a = 5;
b = 20;
if ( a <= b ):
   print "6, a <= b"
else:
   print "6, a >  b"

if ( b >= a ):
   print "7, b >= a"
else:
   print "7, b < a"

print '----------- test 3 -----------'#赋值运算符
# =     简单赋值
# +=    加法赋值
# -=    减法赋值
# *=    乘法赋值
# /=    除法赋值
# %=    取模赋值
# **=   求幂赋值
# //=   整除赋值

a = 21
b = 10
c = 0

c = a + b
print "1, c = ", c

c += a
print "2, c = ", c 

c *= a
print "3, c = ", c 

c /= a 
print "4, c = ", c 

c = 2
c %= a
print "5, c = ", c

c **= a
print "6, c = ", c

c //= a
print "7, c = ", c

print '----------- test 4 -----------'#位运算符
# |      或
# &      与
# ^      异或
# ~      取反
# <<     左移
# >>     右移

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print "1, c = ", c

c = a | b;        # 61 = 0011 1101 
print "2, c = ", c

c = a ^ b;        # 49 = 0011 0001
print "3, c = ", c

c = ~a;           # -61 = 1100 0011
print "4, c = ", c

c = a << 2;       # 240 = 1111 0000
print "5, c = ", c

c = a >> 2;       # 15 = 0000 1111
print "6, c = ", c

print '----------- test 5 -----------'#逻辑运算符
# and    条件与
# or     条件或
# not    条件非

a = 10
b = 20

if ( a and b ):
   print "1, a and b true"
else:
   print "1, a or b not true"

if ( a or b ):
   print "2, a or b true"
else:
   print "2, a and b not true"

a = 0
if ( a and b ):
   print "3, a and b true"
else:
   print "3, a or b not true"

if ( a or b ):
   print "4, a or b true"
else:
   print "4, a and b not true"

if not( a and b ):
   print "5, a or b not true"
else:
   print "5, a and b true"

print '----------- test 6 -----------'#成员运算符
# in     是成员
# not in 非成员

a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print "1, a in list"
else:
   print "1, a not in list"

if ( b not in list ):
   print "2, b not in list"
else:
   print "2, b in list"

a = 2
if ( a in list ):
   print "3, a in list"
else:
   print "3, a not in list"

print '----------- test 7 -----------'#身份运算符
# is          引用自一个对象
# is not      不是引用自一个对象

a = 20
b = 20

if ( a is b ):
   print "1, a and b same"
else:
   print "1, a and b not same"

if ( id(a) is not id(b) ):
   print "2, a and b same"
else:
   print "2, a and b not same"

b = 30
if ( a is b ):
   print "3, a and b same"
else:
   print "3, a and b not same"

if ( a is not b ):
   print "4, a and b not same"
else:
   print "4, a and b same"

print '----------- test 8 -----------'#运算符优先级
# **
# ~ + -
# * / % //
# + -
# >> <<
# &
# ^ |
# <= < > >=
# <> == !=
# = %= /= //= -= += *= **=
# is is not
# in not in
# not or and

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print "(a + b) * c / d = ",  e

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print "((a + b) * c) / d = ",  e

e = (a + b) * (c / d);    # (30) * (15/5)
print "(a + b) * (c / d) = ",  e

e = a + (b * c) / d;      #  20 + (150/5)
print "a + (b * c) / d = ",  e

