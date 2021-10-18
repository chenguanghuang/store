#*encoding=utf-8
from unittest import TestCase
from appium import webdriver
from ddt import ddt
from ddt import data
from day04APPauto.loginOpera import *
from day04APPauto.logintest import InitPage2
import time


data1 = InitPage2().getExcle(path=r"D:\Users\chen\PycharmProjects\ceshi\自动化\day04APPauto\test.xlsx",sheet_name="Sheet1")
@ddt
class Testlogin(TestCase):
    def setUp(self)-> None:
        # 指定设备信息
        device = {}

        device['deviceName'] = '127.0.0.1:62001'
        device['platformName'] = 'Android'
        device['platformVersion'] = '7.1.2'
        device['appPackage'] = 'com.sina.weibo'  # App名称微博
        # device['appActivity']='SplashActivity'  #AppActivity
        device['appActivity'] = '.MainTabActivity'
        device['noRestart'] = True
        # 打开APP
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", device)

    def tearDown(self)-> None:
        self.driver.quit()

    #登录成功的用例
    @data(*data1)
    def testsuccess1(self,testdata):
        #提取数据
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        #调用被被测试类
        loginObj = LoginOpera(self.driver)
        time.sleep(2)
        loginObj.login(username,password)

        # 获取实际结果
        data = loginObj.getSuccessResult()
        #  断言
        self.assertEqual(data,expect)




















