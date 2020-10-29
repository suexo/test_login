import time
import unittest
import sys
sys.path.append('C:\\Users\\exo\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\python')
from HTMLTestRunner import HTMLTestRunner
from crrm.base.opertion_browe import OpertionBrowe
from crrm.base.use_beower import UserBeower
from crrm.web_page.usermanger.login import Login
from crrm.until.exl import OpertionExcel
from crrm.until.yaml import Yamloption


class MyTestCase(unittest.TestCase):

   def setUp(self) -> None:
       self.exl=OpertionExcel('../../config/11.xlsx','用例参数')
       self.login=Login()
       self.ym = Yamloption('../../config/test.yaml')
       self.bo=OpertionBrowe(UserBeower.driver)

   def test_login_usernull(self):
       self.login.login(self.exl.get_cell(1,2),self.exl.get_cell(1,3))
       self.assertEqual(self.bo.login_alert(),self.exl.get_cell(1,4))

   def test_login_passnull(self):
       self.login.login(self.exl.get_cell(2,2),self.exl.get_cell(2,3))
       self.assertEqual(self.bo.login_alert(),self.exl.get_cell(2,4))

   def test_login_error(self):
       self.login.login(self.exl.get_cell(3, 2), self.exl.get_cell(3, 3))
       self.assertEqual(self.bo.login_alert(), self.exl.get_cell(3, 4))

   def test_login_null(self):
       self.login.login(self.exl.get_cell(4, 2), self.exl.get_cell(4, 3))
       self.assertEqual(self.bo.login_alert(), self.exl.get_cell(4, 4))


   def test_login_succed(self):
       self.login.login(self.exl.get_cell(5,2),self.exl.get_cell(5,3))
       value=self.login.login_succed('mainFrame',self.ym.get_locator('LoginPage','loginsu'))
       self.assertEqual(value,self.exl.get_cell(5,4))


   def tearDown(self) -> None:
       UserBeower.quit()

if __name__ == '__main__':
    # unittest.main()
    suite=unittest.TestSuite()
    test_case=unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    suite.addTests(test_case)
    # 获取当前时间
    data_time=time.strftime('%Y-%m-%d',time.localtime())
    # 创建HTML报告
    with open('../../report/report.html','wb+') as file:
       runner=HTMLTestRunner(stream= file,verbosity=1,title=None,description=None)
       runner.run(suite)
