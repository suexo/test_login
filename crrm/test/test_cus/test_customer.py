import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from crrm.base.opertion_browe import OpertionBrowe
from crrm.base.use_beower import UserBeower
from crrm.db.customenr_db.customeroperdb import CusoperationDb
from crrm.until.exl import OpertionExcel
from crrm.web_page.cusmanger.customer import Customer


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.cus=Customer()
        self.db=CusoperationDb()
        self.db.dele()
        self.us=OpertionBrowe(UserBeower.driver)
        self.exl = OpertionExcel("../../config/11.xlsx", '用例参数')

    def test_add_succed(self):
        self.cus.custome(name='s001',data='2020-1-2',email='1135@qq.com',man='exo')
        self.assertEqual(True,self.cus.seach_chack())


    def tearDown(self) -> None:
        UserBeower.quit()

if __name__=='__main__':
    unittest.main()
    # suite=unittest.TestSuite(
    # test_case=unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    # suite.addTests(test_case)
    # # 获取当前时间
    # data_time=time.strftime('%Y-%m-%d',time.localtime())
    # # 创建HTML报告
    # with open('../../report/report_'+data_time+'.html','wb+') as file:
    #    runner=HTMLTestRunner(stream= file,verbosity=1,title=None,description=None)
    #    runner.run(suite)
