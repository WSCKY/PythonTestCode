#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个的元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表


# list.append(x) 	把一个元素添加到列表的结尾,相当于 a[len(a):] = [x].
# list.extend(L) 	通过添加指定列表的所有元素来扩充列表,相当于 a[len(a):] = L.
# list.insert(i, x) 	在指定位置插入一个元素.第一个参数是准备插入到其前面的那个元素的索引,例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x).
# list.remove(x) 	删除列表中值为 x 的第一个元素.如果没有这样的元素,就会返回一个错误.
# list.pop([i]) 	从列表的指定位置删除元素,并将其返回.如果没有指定索引,a.pop()返回最后一个元素.元素随即从列表中被删除.（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号,你会经常在 Python 库参考手册中遇到这样的标记.）
# list.clear()          移除列表中的所有项,等于del a[:].
# list.index(x) 	返回列表中第一个值为 x 的元素的索引.如果没有匹配的元素就会返回一个错误.
# list.count(x) 	返回 x 在列表中出现的次数.
# list.sort()           对列表中的元素进行排序.
# list.reverse() 	倒排列表中的元素.
# list.copy()           返回列表的浅复制，等于a[:].

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x') # 2 1 0
a.insert(2, -1)
a.append(333)
print a # [66.25, 333, -1, 333, 1, 1234.5, 333]
print a.index(333) # 1
a.remove(333)
print a # [66.25, -1, 333, 1, 1234.5, 333]
a.reverse()
print a # [333, 1234.5, 1, 333, -1, 66.25]
a.sort()
print a # [-1, 1, 66.25, 333, 333, 1234.5]

#列表推导式
vect = [2, 4, 6]
print [3 * x for x in vect] # 将列表每个元素 * 3
print [[x, x**2] for x in vect] # 扩展
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print [weapon.strip() for weapon in freshfruit] # 调用方法(去空格)
print [3 * x for x in vect if x > 3] # 使用if子句过滤

vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print [x*y for x in vec1 for y in vec2]
print [x+y for x in vec1 for y in vec2]
print [vec1[i]*vec2[i] for i in range(len(vec1))] # 注意与上面的执行结果区分
# 嵌套函数
print [str(round(355.0/113.0, i)) for i in range(1, 6)] # round() 方法返回浮点数x的四舍五入值.

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print [[row[i] for row in matrix] for i in range(4)] # 转置矩阵


