#*encoding=utf-8
'''

https://www.suning.com/


'''

import time
from selenium import webdriver

#创建浏览器对象
driver = webdriver.Chrome()

#打开网站
driver.get("https://www.suning.com/")
driver.maximize_window()
#定位元素
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("电脑")
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()
#购买商品
time.sleep(2)
driver.find_element_by_xpath("//*[@id='0070702293-10903542294']/div/div/div[1]/div/a/img").click()
#加入购物车

#//*[@id="InitCartUrl"]
hand = driver.window_handles#获取当前的所有句柄
driver.switch_to.window(hand[1])#转换窗口至最高的句柄
driver.find_element_by_xpath("//*[@id='addCart']").click()
#去购物车结算
# driver.switch_to.frame("_fsd")
driver.find_element_by_xpath("/html/body/div[38]/div/div[2]/div/div[1]/a").click()

driver.find_element_by_xpath("//*[@id='cart-wrapper']/div[3]/div/div/div[2]/div[2]/a").click()





time.sleep(2)
#退出浏览器
driver.quit()


















