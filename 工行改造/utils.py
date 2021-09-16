'''保存公共的功能模块'''
import os
import pymysql
host = "localhost"
user = "root"
password = "123"
database = "company"
def get_directory(path):
    '''
    获取指定目录下的所有文件名和目录名
    :param path: 指定目录的路径
    :return: 返回一个列表（包含文件名，目录名）
    '''
    if os.path.exists(path):#检查指定路径是否存在
        if os.path.isdir(path):#检查指定路径是否为目录
            return os.listdir(path)#返回指定目录下的所有文件名和目录名
        else:
            print(f'{path}不是一个目录')
    else:
        print(f'{path}不存在')
    return False

def read_file(path,encoding='utf8'):
    '''
    读取指定文件内容
    :param path: 读取指定文件
    :return: 返回一个列表
    '''
    if os.path.exists(path) and os.path.isfile(path):#检查指定路径是否存在,且是否为文件
        with open(file=path,mode='r',encoding='utf8') as f:
            return f.readlines()
    else:
        print(f'文件{path}错误')
        return False

def is_continue():
    mark = input("继续请输入1，结束请按任意键！")
    if mark !="1":
        return False
    return True

def select(sql, mode="all",size="many"):  #
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql)
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)


def insert(sql,param):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()

    cursor.close()
    con.close()

# sql = "insert into bank (username,account,passwd,country, province, street, door, money, bank)" \
#       " values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# param = ('cc', 19259427, '111111', 'cc', 'c', 'c', 'dd', 10000, '中国工商银行')
#
# insert(sql, param)

