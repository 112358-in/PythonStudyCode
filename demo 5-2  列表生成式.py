# 列表生成式
import random

lst = [ item for item in range(1,10,2)]
print(lst)
lst1 = [ 2*item+1 for item in range(1,10,2)]
print(lst1)

# lst3 = [ random.randint(1,100) for item in range(10)] # 在生成式中不适用item可以使用“_”代替，“_”也可以代表变量
lst3 = [random.randint(1,100) for _ in range(10)]
print(lst3)

# 从列表中筛选符合条件的元素组成新的列表
lst5 = [i for i in range(10) if i%2==0]
print(lst5)

