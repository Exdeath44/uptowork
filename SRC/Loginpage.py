from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint


class Loginpage():

    def __init__(self, driver):
        self.driver = driver

    def turnoffcookies(self):
        self.driver.find_element_by_css_selector("body > div.cc-window.cc-floating.cc-type-info.cc-theme-classic.cc-"
                                                 "bottom.cc-left.cc-color-override--1235852008 > div > a").click()

    def email(self, adresemail):
        emailinput = self.driver.find_element_by_name("email")
        emailinput.send_keys(adresemail)

    def password(self, passtoaccount):
        passwordinput = self.driver.find_element_by_name("password")
        passwordinput.send_keys(passtoaccount)

    def passwordfrommockaroo(self, passmockaroo):
        passwordinput = self.driver.find_element_by_name("password")
        passwordinput.send_keys(passmockaroo + "A" + str(randint(10, 99)))

    def submit(self):
        self.driver.find_element_by_name("submit").click()

    def waituntillloggedin(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "btnUserCreateCV")))

    def signinbutton(self):
        self.driver.find_element_by_css_selector("#auth > div > div > div > div.col-12.offset-sm-2.col-sm-8.offset-lg-2"
                                                 ".col-lg-4 > div:nth-child(1) > a").click()