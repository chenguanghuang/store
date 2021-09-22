import pandas as pd
from day8.DBUtils import *
import xlrd
import time
import pymysql
host="localhost"
user="root"
password = "123"
database = "ceshi"
# database = input("请输入要操作的数据库:")
#database = "company"

f = xlrd.open_workbook('G:/2020年每个月的销售情况.xlsx')
sheets = f.sheets()              # 获取所有的sheet对象
sheet = f.sheet_by_index(0)   # 通过索引获取sheet对象
rows = sheet.nrows                # 返回sheet中的行数
# # cols = sheet.ncols
sheet1 = f.sheet_names()     # 获取sheet名
#
# print(sheet1)
# for k in t:
# t=[]
# t.append(sheet1[0])
# for i in range(1, rows):
#     sql = "INSERT INTO `销售表` SET 月份 =%s"
#     param  = "一月"
#     date = (sheet.row_values(i))
#     time.sleep(0.01)
#     print(t)
    # print(d)
    # sql ="insert into 销售表 values (%s,%s,%s,%s,%s,%s)"
# print(rows)
# print(cols)
# print(sheet)
# print(t)
# print(d)
# print(len(sheets))
# for j in range(0, len(sheets)):
#     sheet = f.sheet_by_index(j)
# print(str(sheet[0]))

def excle_to_date():
    try:
        con = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = con.cursor()
        for j in range(0,len(sheets)):
            date = []
            sheet= f.sheet_by_index(j)
            rows = sheet.nrows  # 返回sheet中的行数
            for i in range(1, rows):
                date.append(sheet1[j])
                date1=(sheet.row_values(i))
                date.extend(date1)
                time.sleep(0.01)
                # print(date)
                sql = "INSERT into `销售表` (`月份`,`日期`,`服装名称`,`价格`,`库存量`,`销售量`) VALUES  (%s,%s,%s,%s,%s,%s)"
                param = (date)
                cursor.execute(sql, param)
                # print(param)
                date.clear()
            j +=1

        con.commit()    #提交操作
        cursor.close()  #关闭游标
        con.close()     #关闭数据库
    except:Exception

# excle_to_date()


# 获取所有表数据
def GetExcle():

    # f = pd.ExcelFile('G:/2020年每个月的销售情况.xlsx')
    # for i in f.sheet_names:
    #     time.sleep(0.1)
    #     d = pd.read_excel('G:/2020年每个月的销售情况.xlsx',sheet_name=i)
    #     print(d)
    #     break
    try:
        a = 0
        d = {}
        for j in range(0, len(sheets)):
            sheet = f.sheet_by_index(j)
            # # name = f.sheet_name()
            # print(sheet)
            rows = sheet.nrows  # 返回sheet中的行数
            for i in range(1, rows):
                date = (sheet.row_values(i))
                #time.sleep(0.01)
                #print(date)
                a += date[2] * date[4]

#---------------------销售额------------------
        print("总销售额为:",round(a,2))
# ---------------------占比------------------
        sql = "SELECT SUM(e.`销售量`) FROM(SELECT * FROM `销售表` WHERE `服装名称` = '羽绒服') e;"

        print("销售占比")

    except:Exception
# a =0
# GetExcle()
# dic = dict()
# f = pd.ExcelFile('G:/2020年每个月的销售情况.xlsx')
# for i in f.sheet_names:
#     d = pd.read_excel('G:/2020年每个月的销售情况.xlsx', sheet_name=i)
#     a += d[2]*d[4]
# print(a)
#GetExcle()

def shujufenxi():
    d = {}
    l = []
    sql = "SELECT SUM(`销售量`) FROM `销售表`"    #(`销售量`)
    date = selectSUM(sql)
    print("销售总额为:",date[0])
    # ---------------------占比------------------
    sql1 = "SELECT SUM(e.`销售量`) FROM(SELECT * FROM `销售表` WHERE `服装名称` = '羽绒服') e;"
    date1 = selectSUM(sql1)
    print(date1[0])
    # ---------------------占比------------------
    print("销售占比:",date1[0]/date[0])
    sql2= "SELECT `服装名称` FROM `销售表` GROUP BY `服装名称`"
    date2 = selectAll(sql2)
    print(date2)


shujufenxi()












