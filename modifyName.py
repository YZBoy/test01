"""
  @Author : Young
  @Email : 1293271923@qq.com
"""
# 批量修改文件名
# 接收2个参数：path-文件夹路径 name-修改后的文件名前缀
import os
import sys

def modify_name(path,name):
	# 1. os.listdir()获取所有文件 2. os.rename()修改文件名
	os.chdir(path)
	i = 1
	for file in os.listdir():
		# print(file)
		if os.path.splitext(file)[1].lower() in [".jpg",".apag",".gif",".jpeg",".png"]:
			os.rename(file, name + "_" + str(i) +".jpeg")
			i =i+1
	print("success!")

if __name__ == "__main__":
	path = sys.argv[1] # 接收第一个参数：文件夹路径
	name = sys.argv[2] # 接收第二个参数：修改后的文件名前缀
	modify_name(path,name)