#!/usr/bin/python3
# -*- coding: UTF-8 -*-

print ("你好，世界")

#定义变量 多个在一行，用;分开
flag_true = True; flag_false = False;
#多个变量赋一个值，分配到相同的内存空间
var_a = var_b = var_c = 1
print(var_a)
print(var_b)
var_d ,var_e,var_f = 1,3,"string var"
print(var_f)
flagTrueFalse = True

if flag_false:
	print ("this is true")
else:
	print ('I am 单引号 ')

item_one = "abc"
item_two = "def"
item_thr = "ghj"

total = item_one + \
		item_two + \
		item_thr
print ( total )

totals = ['itema','itemb','itemc',
			'itemd']
print ( totals ) 



#字符串  不可变 Python 没有单独的字符类型，一个字符就是长度为1的字符串。
#        两种索引方式，从左往右以0开始，从右往左以-1开始。

#三引号
s_lin_str = """ 这是一个三引号字符串
可以多行
嗯，可以多行
"""
print(s_lin_str)

n_str = r"这是一个自然字符串\n"  #自然字符串 r 或者 R
print(n_str)

u_str = u"this is a unicode 字符串" #Unicod 字符串 u或U
print(u_str)

str = 'abcdefgh'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次   字符串可以用+运算符连接在一起，用*运算符重复。
print (str + "TEST") # 连接字符串

#Numbers

#整数 int
intA =1
print (intA)
#在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
intAAA = 890790
print (intAAA)
#浮点数 float
f_a = 1.23
f_b = 3E-2
print(f_a)
print(f_b)
#复数
fl_a = 1+f_a
print(fl_a)

"""
在Python2中是没有布尔型的，它用数字0表示False，用1表示True。到Python3中，
把True和False定义成关键字了，但它们的值还是1和0，它们可以和数字相加。
"""

#del 删除对象
del fl_a,f_a
int_a =2
int_b =4
#除法，得到一个浮点数
print (int_a/int_b)
# 除法，得到一个整数
print(int_a//int_b)
#乘方
print(int_a ** int_b)
#在混合计算时，Python会把整型转换成为浮点数。

"""
列表 List
列表是写在方括号([])之间、用逗号分隔开的元素列表。
元素的类型可以不相同
和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
与Python字符串不一样的是，列表中的元素是可以改变的
"""
list_a = ['abcd',234,2.33,'locea', 23]
list_b = [123,'angela']
print (list_a)            # 输出完整列表
print (list_a[0])         # 输出列表第一个元素
print (list_a[1:3])       # 从第二个开始输出到第三个元素
print (list_a[2:])        # 输出从第三个元素开始的所有元素
print (list_b * 2)    # 输出两次列表
print (list_a + list_b) # 连接列表

"""
元组 Tuple
与字符串一样，元组的元素不能修改
元组也可以被索引和切片，方法一样
注意构造包含0或1个元素的元组的特殊语法规则
也可以使用+操作符进行拼接
可以把字符串看作一种特殊的元组
"""
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

"""
string、list和tuple都属于sequence（序列）
"""

#集合 Sets

#字典 Dictionary


#等待用户输入
you_input_val = input("\n input some value ,then press enter key,exit!\n")
print("you input value is %s"%you_input_val)
