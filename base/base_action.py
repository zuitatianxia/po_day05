from selenium.webdriver.support.wait import WebDriverWait

from base.base_dirver import init_driver

class BaseAction:
    def __init__(self,driver):
        self.driver=driver

    #函数3 输入文本自定义函数 调用函数1
    def input_search_text(self,loc,text):
        self.find_elenent(loc).send_keys(text)

    #自定义函数2（调用函数1）
    def click(self,loc):
        self.find_elenent(loc).click()

    #自定义函数1
    def find_elenent(self,loc):
        by=loc[0]
        value=loc[1]
        return WebDriverWait(self.driver,10,1).until(lambda x:x.find_element(by,value))
        #return self.driver.find_element(by,value)
        #return self.driver.find_element(loc[0], loc[1])

    def find_elenents(self,loc):
        by=loc[0]
        value=loc[1]
        return WebDriverWait(self.driver,5,1).until(lambda x:x.driver.find_elements(by,value))


