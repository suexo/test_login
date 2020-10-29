from selenium.webdriver.common.alert import Alert

class OpertionBrowe:

    def __init__(self,driver):
        self.driver=driver


    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'url地址错误')

    def send_keys(self,xpath,value):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(value)
        except Exception as e:
            print(e,'not find')

    def click(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e, 'not find')

    def get_test(self,xpath):
        try:
            txt=self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            print(e,'not find')
        return txt

    def change_fram(self,frame_name):
        if '/' not in frame_name:
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.frame(frame_name)
        else:
            self.driver.switch_to.parent_frame()
            name = self.driver.find_element_by_xpath(frame_name)
            self.driver.switch_to.frame(name)

    def login_alert(self):
        alert = Alert(self.driver)
        aler_text = alert.text
        alert.accept()
        return aler_text

    def execute_script(self):
        self.driver.execute_script("document.getElementById('customerBirthday').readOnly=false")
    #
    # def select(self):
    #     element=self.driver.find_element_by_xpath()

# 定位元素
# element=driver.find_element_by_id('Selector')
# # 实例化
# select_oper=Select(element)
# # 通过文本选择值
# # select_oper.select_by_visible_text('苹果')
# # 下标选择
# select_oper.select_by_value('orange')
# time.sleep(3)

