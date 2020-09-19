"""
  @Author : Young
  @Email : 1293271923@qq.com
"""
# 连续点击坐标(X,Y)
import os
import time
import sys


def click(X,Y,times):
	for i in range(times):
		os.system("adb shell input tap %d %d"%(X,Y))
		# time.sleep(0.2)
		
if __name__ == "__main__":
	# 接收坐标值X，Y，若没有或输入错误，默认X=100,Y=100
	try:
		X = int(sys.argv[1])
		Y = int(sys.argv[2])
		times = int(sys.argv[3])
	except:
		print("X,Y坐标值使用默认值：X=%s，Y=%s"%(100,100))
		X,Y = 100,100
	print("模拟点击坐标(%s,%s) %s次"%(X,Y,times))
	click(X,Y,times)
