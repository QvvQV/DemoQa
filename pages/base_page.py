#from selenium.webdriver.common.by import By
#import time
import logging
from components.components import WebElement
import requests

class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url #'https://demoqa.com/'



    def visit(self):
        return self.driver.get(self.base_url)
    def request (self):
        request = requests.get(self.base_url)
        return request.status_code == 200



       # if request.status_code == 200:
          #  return True
      #  return False


        #try:
          #  return self.driver.request.get(self.base_url)
       # except requests.exceptions.ConnectionError:
         #   return (f'URL {self.base_url} not reachable')


    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_url(self):
        return self.driver.current_url


    def get_title(self):
        return self.driver.title

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False


    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

        self.metaView = WebElement(driver, 'head > meta')





  #def find_element(self, locator):
     #   time.sleep(3)
     #   return self.driver.find_element(By.CSS_SELECTOR, locator)

