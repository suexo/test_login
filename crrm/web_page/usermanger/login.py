from crrm.base.opertion_browe import OpertionBrowe
from crrm.base.use_beower import UserBeower
from crrm.log_log.auto_html import Autolog
from crrm.until.exl import OpertionExcel
from crrm.until.yaml import Yamloption

class Login:
    def __init__(self):
        self.log=Autolog()
        self.exl = OpertionExcel("../../config/11.xlsx", '用例参数')
        self.ym=Yamloption('../../config/test.yaml')
        self.up=UserBeower()
        self.bo=OpertionBrowe(UserBeower.driver)
        self.bo.open_url(self.exl.get_cell(1,1))

    def login(self, usernam='', passwor=''):
        self.log.set_message('输入用户名'+usernam,'info')
        self.bo.send_keys(self.ym.get_locator('LoginPage','username'),usernam)
        self.log.set_message('输入密码' +passwor, 'info')
        self.bo.send_keys(self.ym.get_locator('LoginPage','password'),passwor)
        self.bo.click(self.ym.get_locator('LoginPage','loginclick'))

    def login_succed(self,frame_name,xpath):
        self.bo.change_fram(frame_name)
        return self.bo.get_test(xpath)






