# 元组
# 1、创建二维元组
# 1.1 方法一：使用小括号创建元组
t = ("hello", ["南京", "上海"], 'C', 3.1415926535897)
print(t)

# 1.2 方法二：使用内置函数tuple()创建元组
t1 = tuple("1234")
print(t1)

t3 = ([10, 20, 30])
print(t3)

# t1 = tuple("hello","word")  #TypeError: tuple expected at most 1 argument, got 2
# print(t1)

# 2、删除元组
testT = "hello"
del testT

# print(testT)    # NameError: name 'testT' is not defined
