#*encoding=utf-8
import xlrd

'''
    数据类，只准备数据集
'''

class InitPage2():
    def getExcle(self,path,sheet_name):
        list_Data = []
        f = xlrd.open_workbook(path)    #读取文件
        sheet = f.sheet_by_name(sheet_name)  #通过sheet名字或得sheet对象
        nor = sheet.nrows #获取sheet中的行数
        nol = sheet.ncols#获取sheet中的列数
        for i in range(1,nor):  #一行一行的获取数据
            dict={}  #将取到的数据存入字典
            for j in range(nol):
                title = sheet.cell_value(0,j)
                value = sheet.cell_value(i,j)
                dict[title] = value
            list_Data.append(dict)
        # print(list_Data)
        return list_Data

# data1 = InitPage2().getExcle(path=r"D:\Users\chen\PycharmProjects\ceshi\自动化\day04APPauto\test.xlsx",sheet_name="Sheet1")






















