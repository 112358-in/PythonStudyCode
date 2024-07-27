import keyword  # 导入Python内置模块

print(keyword.kwlist)   # 获取保留字
                        # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
                        # 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
                        #  'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
                        # 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(len(keyword.kwlist))  # 获取保留字个数 35个