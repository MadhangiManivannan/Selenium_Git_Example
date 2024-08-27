from selenium import webdriver


def test_Google():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    assert driver.title == "Google"
    driver.close()


def test_fb():
    driver = webdriver.Chrome()
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    assert driver.title == "fb"
    driver.close()