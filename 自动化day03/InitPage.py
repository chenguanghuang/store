#*encoding=utf-8
import xlrd
import os
'''
    1.数据类：
        只准备数据，不参与任何操作
    #创建4条用例，两条成功，两条失败
'''
class InitPage:
    login_success_data = []
    f = xlrd.open_workbook(r'D:\Users\chen\PycharmProjects\ceshi\自动化\day03自动化框架\登录测试数据.xlsx')
    sheet = f.sheet_by_name("成功数据")  # 通过索引获取sheet对象
    nor = sheet.nrows # 返回sheet中的行数
    nol = sheet.ncols # 返回sheet中的列数
    dict = {}
    for i in range(1, nor):
        for j in range(nol):
            title = sheet.cell_value(0, j)
            value = sheet.cell_value(i, j)
            # print value
            dict[title] = value
        login_success_data.append(dict)
    # print(login_success_data)

    login_error_data = []
    f = xlrd.open_workbook(r'D:\Users\chen\PycharmProjects\ceshi\自动化\day03自动化框架\登录测试数据.xlsx')
    sheet = f.sheet_by_name("失败数据")  # 通过索引获取sheet对象
    nor = sheet.nrows  # 返回sheet中的行数
    nol = sheet.ncols  # 返回sheet中的列数
    dict = {}
    for i in range(1, nor):
        for j in range(nol):
            title = sheet.cell_value(0, j)
            value = sheet.cell_value(i, j)
            # print value
            dict[title] = value
        login_error_data.append(dict)
    # print(login_error_data)










