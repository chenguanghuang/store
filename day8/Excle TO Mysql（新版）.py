import xlrd
import time
import pymysql
#----------------------------连接数据库-------------------------
host="localhost"
user="root"
password = "123"
# database = "ceshi"
# host = input("请输入要操作数据库host地址:")
# user = input("请输入要操作的数据库用户名:")
# password = input("请输入要操作的数据库密码:")
database = input("请输入要操作的数据库:")
#——————————————————————————获取Excel表数据------------------------
f = xlrd.open_workbook('G:/2020年每个月的销售情况.xlsx')
sheets = f.sheets()              # 获取所有的sheet对象
sheet = f.sheet_by_index(0)      # 通过索引获取sheet对象
rows = sheet.nrows               # 返回sheet中的行数
# # cols = sheet.ncols           # 返回sheet中的列数
sheet1 = f.sheet_names()         # 获取sheet名

#----------------------------定义Excle表到数据库的函数-------------------------
def Excle_to_Mysql():
    try:
        con = pymysql.connect(host=host, user=user, password=password, database=database) #建立数据库连接
        cursor = con.cursor()                                           #建立游标
        for j in range(0, len(sheets)):         #遍历sheet表
            date = []                           #创建date列表
            sheet = f.sheet_by_index(j)         #获取sheet对象
            rows = sheet.nrows                  # 返回sheet中的行数
            for i in range(1, rows):            #遍历sheet表中的数据
                date.append(sheet1[j])          #将遍历sheet表名称传入列表中
                date1 = (sheet.row_values(i))   #获取sheet表中的数据
                date.extend(date1)              #将遍历sheet表数据传入date列表中
                time.sleep(0.01)
                #--------------插入数据库----------------------------------
                # print(date)
                sql = "INSERT into `销售表` (`月份`,`日期`,`服装名称`,`价格`,`库存量`,`销售量`) VALUES  (%s,%s,%s,%s,%s,%s)"
                param = (date)
                cursor.execute(sql, param)
                # print(param)
                date.clear()                    #清空date列表
            j += 1

        con.commit()
        cursor.close()
        con.close()
    except:Exception


#----------------------------调用函数-------------------------
Excle_to_Mysql()



