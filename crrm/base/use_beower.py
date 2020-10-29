from selenium import webdriver


class UserBeower:
     driver = None

     def __init__(self):
         self.driver=webdriver.Chrome('../../chromedriver.exe')
         self.driver.maximize_window()
         UserBeower.driver=self.driver

     @classmethod
     def quit(cls):
         UserBeower.driver.quit()