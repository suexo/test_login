import time
from crrm.db.customenr_db.customeroperdb import CusoperationDb
from crrm.db.dbase import DataBase
from crrm.until.exl import OpertionExcel
from crrm.until.yaml import Yamloption
from crrm.web_page.usermanger.login import Login
import re


class Customer:
    def __init__(self):
        self.lp=Login()
        self.lp.login('admin','123456')
        self.ym=Yamloption('../../config/test.yaml')




    def custome(self,**kwargs):
        self.inpu_v=kwargs
        self.lp.bo.change_fram(self.ym.get_locator('LoginPage','fram1'))
        time.sleep(2)
        self.lp.bo.click(self.ym.get_locator('LoginPage','clientclick'))
        time.sleep(2)
        self.lp.bo.change_fram(self.ym.get_locator('LoginPage','fram2'))
        self.lp.bo.click(self.ym.get_locator('LoginPage','addclick'))
        time.sleep(2)
        self.lp.bo.send_keys(self.ym.get_locator('LoginPage','cuName'),kwargs.get('name',''))
        self.lp.log.set_message('输入客户姓名'+kwargs.get('name',''),'info')
        self.lp.bo.execute_script()
        self.lp.bo.send_keys(self.ym.get_locator('LoginPage', 'cuBirthday'), kwargs.get('data', ''))
        self.lp.log.set_message('输入客户出生日期' + kwargs.get('data', ''), 'info')
        self.lp.bo.send_keys(self.ym.get_locator('LoginPage', 'cuEmail'), kwargs.get('email', ''))
        self.lp.log.set_message('输入客户邮箱' + kwargs.get('email', ''), 'info')
        self.lp.bo.send_keys(self.ym.get_locator('LoginPage', 'cuAddMan'), kwargs.get('man', ''))
        self.lp.log.set_message('输入创建人' + kwargs.get('man', ''), 'info')
        time.sleep(2)
        self.lp.bo.click(self.ym.get_locator('LoginPage','subclick'))

    def seach_chack(self):
        txt_alert=self.lp.bo.login_alert()
        time.sleep(2)
        self.lp.bo.change_fram(self.ym.get_locator('LoginPage','fram3'))
        time.sleep(2)
        self.lp.bo.click(self.ym.get_locator('LoginPage','ckclick'))
        self.lp.bo.change_fram(self.ym.get_locator('LoginPage','fram2'))
        time.sleep(2)
        test=self.lp.bo.get_test(self.ym.get_locator('LoginPage','cktext'))
        print(test)
        lst=re.findall('有 (\d+)条',test)
        n = int(lst[0])+1
        name_txt=self.lp.bo.get_test('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr['+str(n)+']/td[2]/div/span')
        if txt_alert==self.lp.exl.get_cell(6,4) and name_txt==self.inpu_v.get('name'):
            return True












#
# if __name__=='__main__':
#     a=Customer()
#     a.custome(name='s005',data='2020-10-19 08:39:25 ',email='1135@qq.com',man='exo')
#     a.seach_chack()

