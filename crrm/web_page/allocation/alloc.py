import time
from crrm.until.yaml import Yamloption
from crrm.web_page.usermanger.login import Login


class Allocatione:
        def __init__(self):
            self.lp = Login()
            self.lp.login('admin', '123456')
            self.ym = Yamloption('../../config/test.yaml')


        def ation(self):
            self.lp.bo.change_fram('/html/frameset/frameset/frame[1]')
            time.sleep(2)
            self.lp.bo.click('//*[@id="submenu1"]/div/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td/span/a')
            time.sleep(2)
            self.lp.bo.change_fram(self.ym.get_locator('LoginPage','fram2'))
            self.lp.bo.click('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[9]/div/span/a')
            time.sleep(2)




