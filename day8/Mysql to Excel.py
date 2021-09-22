import pandas as pd
import pymysql
def Mysql_to_Excel():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123',
            port=3306,
            database='ceshi'
        )
        df = pd.read_sql('''select * from tese''',con=conn)
        df.to_excel("ceshi.xlsx",index=False)
    except:Exception
Mysql_to_Excel()




