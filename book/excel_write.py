"""
  @Author : Young
  @Email : 1293271923@qq.com
"""
# ---Excel文档数据写入
import xlsxwriter
import sys

def write_excel(file_name):
	workbook = xlsxwriter.Workbook(file_name)
	# 创建工作表
	worksheet1 = workbook.add_worksheet('student')
	worksheet2 = workbook.add_worksheet('animal')
	# 写单元格
	list_column = ["id","name","class","data"]
	for i in range(len(list_column)):
		worksheet1.write(0,i,list_column[i])
	# worksheet.write(0, 0, 'id')
	# worksheet.write(0,1, 'name')
	# worksheet.write(0,2, 'class')
	# worksheet.write(0,3, 'data')

	# 写行
	worksheet1.write_row(1, 0, [1, 2, 3])
	# 写列,其中列D需要大写
	worksheet1.write_column('D2', ['a', 'b', 'c'])
	# 关闭工作簿
	workbook.close()

if __name__ == "__main__":
	# 接收工作簿名称
	file_name = sys.argv[1]
	write_excel(file_name)