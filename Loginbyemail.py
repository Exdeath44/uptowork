from selenium import webdriver
from SRC.Initiatetest import Initiatetest
from SRC.Loginpage import *


def login(browser):
    inic = Initiatetest()
    driver = inic.initiate(browser)

    assert "Log In | Zety" in driver.title
    print("Title is OK")
    assert "Log In" in driver.page_source

    lp = Loginpage(driver)
    lp.turnoffcookies()

    lp.email("waclaw.zurko@gmail.com")
    lp.password("cde3$RFV")
    lp.submit()
    lp.waituntillloggedin()

    assert "User's panel | Zety" in driver.title
    assert "My plan" in driver.page_source
    print("Login to page - OK")

    driver.close()


if __name__ == "__main__":
    login(browser=1) #zmieniajac ta zmienna na 0 odpalimy test na headless chrome
