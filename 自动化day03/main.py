#*encoding=utf-8
import HTMLTestRunner #运行器
import unittest
import os
# path =r"D:\Users\chen\PycharmProjects\ceshi\自动化\day03"
#1.加载所有用例
tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

#2.使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "HKR登陆测试",
    description = "HKR登陆详细测试【成功，失败】",
    verbosity = 1,
    stream = open(file="HKR测试报告.html", mode="wb")
)
#3.运行所有用例
runner.run(tests)
