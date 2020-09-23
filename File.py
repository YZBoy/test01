import csv
from pandas import DataFrame
import pandas as pd

result = [{"name":"zy","content":"hi tieba","time":"2018-08-08"},\
          {"name":"yzj","content":"learn python language","time":"2020-02-02"}]
d = {"name":"lee","content":"make money"}
d1 = {"name":"lee","content":"make money","age":10}

# csv文件的写入
with open("test01.csv","w",newline='',encoding="utf-8") as f: # 加入参数newline='' ：避免出现空行
    # fieldnames定义列名
    writer = csv.DictWriter(f,fieldnames=['name','content','time'])
    # 写入列名
    writer.writeheader()
    # 写入包含字典的列表(字典的key在列名中要能找到)
    writer.writerows(result)
    # 写入单个字典
    writer.writerow(d)
    # writer.writerow(d1) #字典的key不在列名中时会报错

# csv文件的读取
with open("test01.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print("name:{}".format(row["name"]),"content:{}".format(row["content"]),"time:{}".format(row["time"]))

# 文本文件写入
with open("test01.txt","w",encoding="utf-8") as f:
    f.write("123\n")
    # 写入一个string
    f.write("456")
    # 写入一个list，list元素必须是string类型
    f.writelines(["123","456\n","写入一个字符串"])
    f.writelines(["abc","def"])

# 文本文件读取
with open("test01.txt","r",encoding="utf-8") as f:
    print(f.read())
    print("--"*10)
    # 游标置于文件开头
    f.seek(0)
    # 遍历读取每一行
    for line in f:
        print(line,end="")
    f.seek(0)
    print("--"*10)
    # readlines()读取文件所有内容返回一个list，每一行为list的一个元素
    print(f.readlines())
    f.seek(0)
    print("--"*10)
    # readline() 每次只读取一行
    print(f.readline(),end="")
    print(f.readline())


# excel文件写入
data = {
    'name':['zy','xmq','tt'],
    'age':[18,28,8],
    "sex":['male','female','male']
}
df = DataFrame(data)
df.to_excel('test01.xlsx')

# excel文件读取
df = pd.read_excel('test01.xlsx')
print(df)
for key in df:
    print("---" * 10)
    print(key,type(key))
    print(df[key],type(df[key]))