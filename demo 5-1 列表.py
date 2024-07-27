# 1、定义一个序列lst，并声明lst序列元素
lst = [10, 20, 30, 40, 50, 100]

# 输出lst列表，及lst列表地址
print(lst, id(lst))

# 2、对lst列表进行排序
# 2.1 使用sort()函数进行排序操作
# 默认升序 使用sort(self,key,reverse)  其中reverse=False为升序，reverse=True为降序
lst.sort()
print("升序：", lst)

# 降序
lst.sort(reverse=True)
print("降序：", lst)

# 2.2 使用sorted()函数进行排序操作
# sorted(列表)
fruits = ["banana", "ZZZ", "apple", "fff"]
asc_fruits = sorted(fruits)
desc_fruits = sorted(fruits, reverse=True)
print("升序：", asc_fruits)
print("降序：", desc_fruits)
print("原列表：", fruits)

# 忽略大小写进行排序“key=str.lower”
asc_fruits = sorted(fruits, key=str.lower)
print(asc_fruits)

# range()函数
# for i in range(0, 9):
#     print(i)

'''
range()函数的用法：
1.Python内置函数
2.python2.x range() 函数可创建一个整数列表，一般用在 for 循环中
3.Python3 range() 返回的是一个可迭代对象（类型是对象）

函数语法：
range(start, stop[, step])

参数说明：
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
'''