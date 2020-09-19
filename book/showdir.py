"""
  @Author : Young
  @Email : 1293271923@qq.com
"""
# 实现树形打印目录结构 

import os
import sys

def showdir(path):
	for root,dir,file in os.walk(path):
		file_name = root.split("\\")[-1]
		deep = len(root.split("\\")) - len(path.split("\\"))
		print("| "*deep+"+--"+file_name)
		for i in file:
			print("| "*(deep+1)+"+--"+ i)
		
if __name__ == "__main__":
	#接收一个参数：目录路径
	path = sys.argv[1]
	showdir(path)