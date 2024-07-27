# 闰年 能被4整除不能被100整除或能被400整除
i = eval(input("请输入年份："))
if (i%4 == 0 and i%100 != 0) or (i%400==0):
    print(i,'是闰年')
else:
    print(i,'不是闰年')