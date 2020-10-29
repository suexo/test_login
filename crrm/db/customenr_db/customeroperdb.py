from crrm.db.dbase import DataBase


class CusoperationDb:
    def __init__(self):
        self.db=DataBase(host='localhost', user='root',password='123456', database='crm', port=3306, charset='utf8')

    def dele(self):
        self.db.update("DELETE FROM customer_info where customer_name='s001';")
