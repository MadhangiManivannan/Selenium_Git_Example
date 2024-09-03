import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def test_setUp():
    global  driver
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield
    driver.close()

@allure.description("OrangeHRM valid credential")
@allure.severity(severity_level="Critical")
def test_validCredentials(test_setUp):
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[normalize-space(text()='Login')]").click()
    homepage_title = driver.title
    assert homepage_title == "OrangeHRM"
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
    driver.find_element(By.LINK_TEXT,"Logout").click()
    driver.close()