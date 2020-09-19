"""
  @Author : Young
  @Email : 1293271923@qq.com
"""

# ---Excel文档数据读取

# 1.导入pandas库
import pandas as pd
import os
import sys

def read_excel(path):
	# 2.pandas.read_excel()方法读取xlsx文档
	df = pd.read_excel(path) #["student","animal"]
	print("输出列标题",df.columns.values)
	print(df,type(df))
	# data1 = df.head(2)
	# 3. 类pandas.core.frame.DataFrame对象数据 通过values属性 转为 类numpy.ndarray对象数据
	data2 = df.values
	# print(data1,type(data1))
	print(data2,type(data2))
	# 4.将numpy.ndarray对象用tolist()方法转为list
	list_data2 = data2.tolist()
	print(list_data2,type(list_data2))
	
if __name__ == "__main__":
	# 接收一个excel文件路径
	path = sys.argv[1]
	read_excel(path)