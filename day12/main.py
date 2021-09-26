'''
    报告：
    1.加载器  负责扫描和加载测试用例
    2.使用运行器运行这些测试用例，并生成测试报告。

'''
import HTMLTestRunner #运行器
import unittest

#1.加载所有用例
pwd = r"D:\Users\chen\PycharmProjects\ceshi\day13"   #
# tests = unittest.defaultTestLoader.discover(r"D:\Users\chen\PycharmProjects\ceshi\day12",pattern="danyuanceshi.py")
tests = unittest.defaultTestLoader.discover(pwd,pattern="TestCalc.py")

#2.使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是一份计算器的测试报告",
    description = "这只是加法运算的测试报告",
    verbosity = 1,
    stream = open("计算器.html",mode="wb")

)

#3.运行所有用例
runner.run(tests)






