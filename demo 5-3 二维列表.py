lst = [
    ["上海","北京","南京"],
    ["长江","黄河","乌江"],
    ["黄山","嵩山","华山"],
    ["康师傅","哇哈哈","三得利"]
]

print(lst)

# 使用双层for循环遍历二维列表
for i in lst:
    for j in i:
        print(j,end='\t')
    print()

# 生成二维列表
lst1 = [ [j for j in range(5)] for i in range(6)]
print(lst)
