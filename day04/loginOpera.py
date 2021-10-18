#*encoding=utf-8
'''
    2.登录操作类：
       只有页面登录的操作

'''
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class LoginOpera:
    # driver声明一个全局变量
    def __init__(self,driver):
        self.driver = driver  # 将传入的driver变成全局的driver浏览器对象

    def login(self,username,password):  #username,password
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

        el1 = self.driver.find_element_by_id("com.sina.weibo:id/titleBack")
        el1.click()
        time.sleep(2)
        el2 = self.driver.find_element_by_id("com.sina.weibo:id/iv_login_view_protocol")
        el2.click()
        time.sleep(2)
        el3 = self.driver.find_element_by_id("com.sina.weibo:id/iv_psw")
        el3.click()
        time.sleep(2)
        el4 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_uname")
        el4.click()
        time.sleep(2)

        el5 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_uname")
        el5.send_keys(username)   #"k1342493938@163.com"
        time.sleep(2)
        el5 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_psw")
        el5.click()
        time.sleep(2)
        el6 = self.driver.find_element_by_id("com.sina.weibo:id/et_login_view_psw")
        el6.send_keys(password)
        time.sleep(2)
        el7 = self.driver.find_element_by_id("com.sina.weibo:id/btn_login_view_psw")
        el7.click()
        time.sleep(2)
        el8 = self.driver.find_element_by_id("com.sina.weibo:id/et_input")
        time.sleep(2)
        answer = input("请输入验证码：")
        el8.send_keys(answer)
        el8.click()
        time.sleep(2)
        el9 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[3]")
        el9.click()
        time.sleep(2)
        el10 = self.driver.find_element_by_id("com.sina.weibo:id/btn_login_view_psw")
        el10.click()

    def getSuccessResult(self):
        return self.driver.current_activity



