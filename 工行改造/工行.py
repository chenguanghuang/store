import random
from python_based.数据结构.utils import *
print(
    '''    ************************************
    *       中国工商银行                 *
    *       账户管理系统                 *
               V1.0                    *
    ***********************************

    *1.开户                             *
    *2.存钱                             *
    *3.取钱                             *
    *4.转账                             *
    *5.查询                             *
    *6.bye                             *'''
)
bank = {}
bank_name = "中国工商银行"

#****************************************************
def bank_user(acount,name,passwd,country,province,street,door,money):
    if len(bank) >100:
        return 3
    if name in bank:
        return 2
    bank[name]={
        "account":acount,
        "passwd":passwd,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":money,
        "bank_name":bank_name
    }
    return 1

#*************************开户************************
def register():
    name = str(input('请输入姓名:'))
    passwd = input('请输入6位数的密码:')
    if check_str(passwd,6):
        pass
    else:
        print("请输入6位数字的密码")
        return 3
    print("请输入地址！！！！")
    country = str(input("国家:"))
    province = str(input("省份:"))
    street = str(input("街道:"))
    door = str(input("门牌号:"))
    money = int(input("请输入预存金额:"))
    acount = random.randint(10000000, 99999999)
    status=bank_user(acount,name,passwd,country,province,street,door,money)
    if status == 1:
        print("开户成功!!!")
        info = '''
            -------------账户信息-------------
            账户：%s
            户名：%s
            密码：******
            国家：%s
            省份：%s
            街道：%s
            门牌号：%s
            账户余额：%s
            开户行：%s
        '''
        print(info % (acount, name, country, province, street, door, money, bank_name))
    elif status == 2:
        print("用户已存在!!!!")
    elif status == 3:
        print("已注册满!!!!!")
#************************判断密码长度******************
def check_str(s: str, l: int):

    # s:待检查的字符串
    # l:待检查的字符串长度
    if s.isalnum() and len(s) == l:
        return True
    else:
        return False
#***********************存钱*************************
def save():
    acount = input("请输入存钱账户:")
    if acount in bank:
        inmoney =int(input("请输入金额:"))
        bank.get(acount)["money"]+= inmoney
        print(bank.get(acount)["money"])
    else:
        return False
#************************取钱************************
def take():
    acount = input("请输入取钱账户:")
    if acount in bank:
        takepasswd = input("请输入密码:")
        if takepasswd == bank.get(acount)["passwd"]:
            outmoney = int(input("请输入金额:"))
            # bank.get(acnout)["money"] -= outmoney
            # print("您的余额为：",bank.get(acnout)["money"])
            if outmoney <= bank.get(acount)["money"]:
                bank.get(acount)["money"] -= outmoney
                print("您的余额为：",bank.get(acount)["money"])
            else:
                print("余额不足！！！")
    else:
        print("账户不存在！！！！")
        take()
#************************转账************************
def trans():
    acount1 = input("请输入转入账户:")
    if acount1 in bank:
        acount2 = input("请输入转出账号:")
        transpasswd = input("请输入账户密码:")
        if transpasswd == bank.get(acount2)["money"]:
            joinmoney = int(input("请输入金额:"))
        # bank.get(acnout)["money"] -= outmoney
        # print("您的余额为：",bank.get(acnout)["money"])
            if joinmoney <= int(bank.get(acount2)['money']):
                bank.get(acount1)["money"] += joinmoney
                bank.get(acount2)["money"] -= joinmoney
                print("您的余额为：", bank.get(acount2)["money"])
            else:
                print("余额不足！！！")
    else:
        print("账户不存在！！！！")

#************************查询************************
def search():
    acount = input("请输入查询账号:")
    if acount in bank:
        takepasswd = input("请输入密码:")
        if takepasswd == bank.get(acount)["passwd"]:
            print(bank)
            print('''-------------账户信息-------------'''
            "账户：",acount,
            "国家：", bank.get(acount)["country"],
            "省份：", bank.get(acount)["province"],
            "街道：", bank.get(acount)["street"],
            "门牌号：", bank.get(acount)["door"],
            "账户余额：", bank.get(acount)["money"],
            "开户行：", bank_name
            )
        else:
            print("密码错误！！！！")
    else:
        print("账户不存在！！！！")

def inMysql():
     date = []
     for k in bank.keys():
        date.append(k)
        for v in bank.values():
            for v1 in v.values():
                date.append(v1)
     # dates = (date[0],date[1],date[2],date[3],date[4],date[5],date[6],date[7],date[8])
     print(date)
     sql = "insert into bank (username,account,passwd,country, province, street, door, money, bank)" \
          " values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     param = date
     insert(sql,param)
     bank.clear()
     date.clear()




while True:
    choice = input("请选择:")
    if choice == '1':
        register()
        inMysql()

    elif choice == '2':
        save()
    elif choice == '3':
        take()
    elif choice == '4':
        trans()
    elif choice == '5':
        search()
    elif choice == '6':
        break
    else:
        print('选择错误')
# ********************************************



