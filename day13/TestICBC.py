from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from day13.ICBC import *
import xlrd



'''
 ['chen', '111111', 'China', 'cishuan', 'kuanzhai', 'c0001', 2000.0, 1.0],
    ['xiaochen', '222222', 'China', 'guangzhou', 'tianhe', 'g0001', 2000000.0, 1.0],
    ['cc', '111111', 'cc', 'c', 'cc', 'c', 2000.0, 1.0]
'''

da = []
f = xlrd.open_workbook("D:/Users/chen/PycharmProjects/ceshi/day13/测试参数.xlsx")
sheet = f.sheet_by_index(0) #通过索引获取sheet对象
row = sheet.nrows #返回sheet中的行数
for i in range(1,row):
    da.append(sheet.row_values(i))
print(da)

@ddt
class TestICBC(TestCase):
    @data(*da)
    @unpack
    def testAddUser(self, a,b,c,d,e,f,g,h):
        s = bank_addUser(a,b,c,d,e,f,g)
        self.assertEqual(s,h)



# da =[]
# f = xlrd.open_workbook("D:/Users/chen/PycharmProjects/ceshi/day13/取钱测试.xlsx")
# sheet = f.sheet_by_index(0)
# row = sheet.nrows
# for i in range(0,row):
#     da.append(sheet.row_values(i))
# print(da)
#
# @ddt
# class TestICBC(TestCase):
#     @data(*da)
#     @unpack
#     def testtakemoney(self, a, b, c, d):
#         t = bank_takeMoney(a, b, c)
#         self.assertEqual(t, d)



