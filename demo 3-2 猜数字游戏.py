# 猜数字
import random

random = random.randint(1,100) # 产生随机整数
count = 0
while 1:
    count += 1
    i = eval(input("请输入："))
    if i < 1 or i > 100:
        print("输入有误")
        continue
    elif random == i:
        print("猜对了，一共猜了",count,"次")
        isSussal = 0
        break
    elif random < i:
        print("大了,",end='')
        continue
    elif random > i:
        print("小了,",end='')
        continue