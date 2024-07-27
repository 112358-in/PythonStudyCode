# 1、for语句使用
# 1.1 for语句
# for 变量 in 字符串/值域:
#    语句块
for i in 'hello':
    print(i)

for i in range(0,10):
    print(i)
# 1.2 for else语句
"""
for 变量 in 遍历对象:
    语句1
else:
    语句2
"""

# 2、if语句使用
# 1.2 if语句
"""
if 变量/条件语句:
   语句块1
else:
   语句块2
"""

# 示例：
i = 4
if i%2==0:
    print(i,"是偶数")

# 2.2 if else 语句
"""
if 变量/条件语句 ... else ...
   语句块
"""
# 示例：
i = 3
if i%2==0:
    print(i,"是偶数")
else:
    print(i,"不是偶数")

# 3、while语句使用
# 3.1 while语句
"""
while 变量:
    主体主体主体
"""
# 示例：
y=3
while y:
    print("这里是while循环主体！")
    y -=1

# 3.2 while语句
"""
while 变量:
    语句1
else:
    语句2
"""
# 示例：
y=1
while y:
    print("好好学习")
    y -=1
else:
    print("天天向上")   # while正常执行完后执行else

# 示例：
y=1
while y:
    print("好好学习")
    break   # 执行break，结束while循环，不会再执行else
else:
    print("天天向上")
