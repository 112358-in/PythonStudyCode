import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
max_value1 = np.max(array)  # 获取数组中的最大值
max_value2 = array.max  # 获取数组中的最大值
max_value3 = array.max()  # 获取数组中的最大值
print(max_value1, max_value2, max_value3)

"""
6 
<built-in method max of numpy.ndarray object at 0x00000199BB886630> 
6
"""