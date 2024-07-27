# 字典

# 1、创建字典
# 1.1 使用{}直接创建字典
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 1.2 通过映射函数创建字典
list1 = (1, 2, 3, 4, 5)
list2 = ('A', 'B', 'C', 'D', 'E')
dObj = zip(list1, list2)   # <zip object at 0x0000014645B31BC0>
# print(list(dObj))          # [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')] --元组类型

# 1.3 通过内置函数dict()创建字典
# d = dict(list1=list2)   # {'list1': ('A', 'B', 'C', 'D', 'E')}
d = dict(dObj)          # {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}  --字典类型
print(d)
# 2、
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print(d)
