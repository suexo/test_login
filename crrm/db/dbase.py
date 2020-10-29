import pymysql


class DataBase:
    #创建连接
    def __init__(self,host,user,password,port,database,charset):
        self.host=host
        self.user=user
        self.password=password
        self.port=port
        self.database=database
        self.charset=charset

    def get_conn(self):
        #创建游标
        try:
            self.conn = pymysql.Connection(host=self.host, user=self.user,
                                           password=self.password, database=self.database
                                           , port=self.port, charset=self.charset)
            return self.conn
        except Exception as e:
            print(e,'Error')

    def serch_data(self,sql):
        try:
            self.conn=self.get_conn()
            self.cur=self.conn.cursor()
            self.cur.execute(sql)
            self.res=self.cur.fetchall()
        except Exception as e:
            print(e, 'Error')
            self.conn.rollback()
        finally:
            self.cur.close()
            self.conn.close()
        return self.res



    def update(self,sql):
        try:
            self.conn = self.get_conn()
            self.cur = self.conn.cursor()
            self.count=self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.cur.close()
            self.conn.close()

        return self.count



# if __name__=='__main__':
#     a=DataBase(host='localhost', user='root',password='123456', database='crm', port=3306, charset='utf8')
#     print(a.update("update customer_info set source_id='1' where customer_name='李四';"))
#     print(a.serch_data("SELECT * FROM customer_info where customer_name='李四';"))

