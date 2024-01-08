from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.soap import SoapHelper


class Application():

    def __init__(self, browser, config):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognize browser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.soap = SoapHelper(self)
        self.config = config
        self.baseUrl = config['web']['baseUrl']




    def open_home_page(self):
        driver = self.driver
        driver.get(self.baseUrl)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
       self.driver.quit()

