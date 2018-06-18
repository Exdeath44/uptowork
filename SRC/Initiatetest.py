from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
linkadres = os.path.dirname(os.path.realpath(__file__)) + "/link.txt"
chromedriveradres = os.path.dirname(os.path.realpath(__file__))


class Initiatetest():

    def __init__(self):
        self.link = ""

    def initiate(self, browser):

        if browser == 0: #headless chrome
            c = open(linkadres, "r")
            link = c.read()
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--window-size=1920x1080")
            driver = webdriver.Chrome(chromedriveradres + '\chromedriver.exe',
                chrome_options=chrome_options)
            print(link)
            self.link = link
            driver.get(link)
            c.close()

        else: #zwykly chrome
            c = open(linkadres, "r")
            link = c.read()
            self.link = link
            driver = webdriver.Chrome(chromedriveradres + '\chromedriver.exe')
            driver.maximize_window()
            driver.get(link)
            c.close()

        return driver
