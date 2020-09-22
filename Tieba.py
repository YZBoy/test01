"""
https://tieba.baidu.com/p/6972849748?red_tag=2913427813
1.在浏览器中查看网页源代码
2.使用python读文本文件
3.正则表达式的应用
4.先抓大再抓小的匹配技巧
5.使用Python写CSV文件
"""
import re
import csv

path = r"C:\Users\Administrator\Desktop\source.txt"
with open(path,"r",encoding="utf-8") as f:
    content = f.read()
pattern_user = 'username="(.*?)"'
pattern_content = '(\S*?)</div><br>'
result_user = re.findall(pattern_user, content, re.S)
result_content = re.findall(pattern_content, content, re.S)
print(result_user,len(result_user))
print(result_content,len(result_content))

# 结果内容：包含字典的列表
# result = []

with open("tieba.txt","w",encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=['姓名','内容'])
    writer.writeheader()
    writer.writer(result)
    
    