'''
    单元测试：
        1、使用unittest单元组件
            1.1继承TestCase测试用例
            1.2测试用例方法命名必须是testxxxx
            1.3使用assertEqual()来断言

'''

from Calc import Calc
import unittest
class TestCalc(unittest.TestCase):

    def testAdd(self):
        #1.准备数据
        a = 6
        b = 5
        c = 11

        #2.调用被测程序
        calc = Calc()
        sum = calc.add(a,b)

        #3.断言
        self.assertEqual(c,sum)

    def testAdd1(self):
        #1.准备数据
        a = -6
        b = -5
        c = 11

        #2.调用被测程序
        calc = Calc()
        sum = calc.add(a,b)

        #3.断言
        self.assertEqual(c,sum)

    def testmulti(self):
        #1.准备数据
        a = -6
        b = -5
        c = 30

        #2.调用被测程序
        calc = Calc()
        sum = calc.multi(a,b)

        #3.断言
        self.assertEqual(c,sum)
    def testdevi(self):
        #1.准备数据
        a = 30
        b = 5
        c = 6

        #2.调用被测程序
        calc = Calc()
        sum = calc.devi(a,b)

        #3.断言
        self.assertEqual(c,sum)

