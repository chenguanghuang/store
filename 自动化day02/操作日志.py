#*encoding=utf-8
import pymysql
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
#创建浏览器对象
driver = webdriver.Chrome()
click = ActionChains(driver)
#打开网站
driver.get("http://localhost:8080/HKR/")
#浏览器最大化
driver.maximize_window()
#选择教师登录
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()
#输入账户和密码
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("jason")
driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")
#点击登录
driver.find_element_by_xpath("//*[@id='submit']").click()
#-----------------------------------教师操作--------------------------
class TeacherOpe():
    def __init__(self):
        #点击教师管理
        driver.find_element_by_xpath("//*[@id='_easyui_tree_11']/span[4]/a").click()
        #设置时延
        time.sleep(0.5)
        #输入教师姓名
        driver.find_element_by_xpath("//*[@id='sear_teaname']").send_keys("曹士明")
        #点击查询
        driver.find_element_by_xpath("//*[@id='search_user']/span").click()
        #重置密码
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='datagrid-row-r1-2-0']/td[9]/div/a").click()
        #关闭弹窗
        driver.switch_to.alert.accept()
        time.sleep(1)
#-----------------------------------学生管理--------------------------
class StudentOpe():
    def __init__(self):
        #点击学生管理
        driver.find_element_by_xpath("//*[@id='_easyui_tree_12']").click()
        #设置时延
        time.sleep(0.5)
        #输入学生姓名
        driver.find_element_by_xpath("//*[@id='J-stu']").send_keys("张伟")
        #点击查询
        driver.find_element_by_xpath("//*[@id='stu_panel']/div/div/div[1]/table/tbody/tr/td[4]/a/span").click()
        time.sleep(1)
        #关闭学生窗口
        driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()
        time.sleep(1)
        #再次点击学生管理
        driver.find_element_by_xpath("//*[@id='_easyui_tree_12']").click()
        #设置时延
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='J-phone']").send_keys("13811234532")
        #点击查询
        driver.find_element_by_xpath("//*[@id='stu_panel']/div/div/div[1]/table/tbody/tr/td[4]/a").click()
        #设置毕业
        driver.find_element_by_xpath("//*[@id='datagrid-row-r2-2-0']/td[11]/div").click()
        #关闭弹窗
        driver.find_element_by_xpath("/html/body/div[8]/div[3]/a").click()
        #关闭窗口
        driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()
# -----------------------------------课程管理--------------------------
class CurseOpe():
    def __init__(self):
        # 点击课程管理
        driver.find_element_by_xpath("//*[@id='_easyui_tree_13']").click()
        # 点击添加课程
        # driver.find_element_by_xpath("//*[@id='tt']/div[2]/div[2]/div").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span").click()
        # 输入课程名
        driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[1]/td[2]/input").send_keys("道德经")
        # 输入课程描述
        driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[2]/td[2]/textarea").send_keys("老子真牛逼")
        # 点击添加
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/a[1]/span").click()
        time.sleep(1)
        # 关闭弹窗
        driver.find_element_by_xpath("/html/body/div[10]/div[3]/a").click()
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/a[2]/span").click()
        time.sleep(1)
        # 关闭窗口
        driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()
#-----------------------------------历史日志操作--------------------------
class HistoryOpe():
    def __inti__(self):
        #点击历史操作日志
        driver.find_element_by_xpath("//*[@id='_easyui_tree_18']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='history']").click()
        #点击下一页
        # driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[10]/a/span/span[2]").click()
        #输入页数
        # driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[7]/input").click()
        doubleclick = driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[7]/input")
        click.double_click(doubleclick).perform()
        driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[7]/input").send_keys("56")
        driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[7]/input").send_keys(Keys.ENTER)
        driver.find_element_by_xpath("//*[@id='history']/div/div/div[1]/table/tbody/tr/td[4]/a/span").click()
        time.sleep(2)
        #关闭当前窗口
        driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()
        #退出系统
        driver.find_element_by_xpath("//*[@id='top']/div/a[2]/img").click()
if __name__ == '__main__':

    # T1 = TeacherOpe()
    # S1 = StudentOpe()
    C1 = CurseOpe()
    # H1 = HistoryOpe()

time.sleep(3)
driver.quit()
