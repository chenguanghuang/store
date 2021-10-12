#*encoding=utf-8
# '''
#     2.登录操作类：
#         只有页面登录的操作
#
#
#
# '''
from  selenium import webdriver

class LoginOpera:
    #driver声明一个全局变量
    def __init__(self,driver):
        self.driver = driver  #将传入的driver变成全局的driver浏览器对象


        #登录的实际操作
    def login(self,username,password):
        self.driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password)

        self.driver.find_element_by_xpath("//*[@id='submit']").click()
    #获取成功的实际结果
    def getSuccessResult(self):
        return self.driver.title
    #获取失败的实际结果
    def getErrorResult(self):
        return self.driver.find_element_by_xpath("//*[@id='msg_uname']").text









