from selenium import webdriver
from SRC.Initiatetest import Initiatetest
from SRC.Loginpage import *
import requests


def register(browser):
    inic = Initiatetest()
    driver = inic.initiate(browser)

    assert "Log In | Zety" in driver.title
    print("Title is OK")
    assert "Log In" in driver.page_source

    lp = Loginpage(driver)
    lp.turnoffcookies()
    lp.signinbutton()
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "terms")))
    assert "Sign Up | Zety" in driver.title
    assert "I have read the " in driver.page_source
    print("Sign up page title is OK")

    r = requests.get("https://my.api.mockaroo.com/my_saved_schema.json?key=d632fae0")
    data = r.text
    data = data.split(",")
    tab = []
    for line in data:
        tab.append(line)

    driver.find_element_by_name("terms").click()
    lp.email(tab[0])
    lp.passwordfrommockaroo(tab[1])
    lp.waituntillloggedin()
    assert "User's panel | Zety" in driver.title
    assert "My plan" in driver.page_source
    print("Sign up - OK")

    driver.close()


if __name__ == "__main__":
    register(browser=1)  # zmieniajac ta zmienna na 0 odpalimy test na headless chrome