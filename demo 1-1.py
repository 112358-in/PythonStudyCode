# test program

"""
使用for循环打印输出：
*****
*****
*****
"""
for i in range(1,4):
    for j in range(1,6):
        print("*", end='')
    print()
print("---------------------")
"""
输出：
*
**
***
"""
j = 7   # 行数
for i in range(1,j):
    for j in range(1,i+1):
        print("*", end='')
    print()
print("---------------------")
"""
输出：
*****
****
***
**
*
"""
for i in range(1,6):
    for j in range(1,7-i):
        print("*",end="")
    print()
print("---------------------")
"""
输出：
   *
  ***
 ******
********
"""
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
print("---------------------")
"""
输出：
   *
  ***
 *****
*******
 *****
  ***
   *
"""
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1,2*i):
        print('*',end='')
    print()
for i in range(1,6):
    for j in range(1,i):
        print(" ", end='')
    for j in range(1,2*(6-i)):
        print("*", end='')
    print()
print("---------------------")
"""
输出：
   *
  * *
 *   *
*     *
 *   *
  * *
   *
"""