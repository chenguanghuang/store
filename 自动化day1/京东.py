import time
from selenium import webdriver

#创建浏览器对象
driver = webdriver.Chrome()

#打开网站
driver.get("https://www.jd.com")

#定位元素
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_c']").send_keys("电脑")
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()
time.sleep(2)
#退出浏览器
# driver.quit()