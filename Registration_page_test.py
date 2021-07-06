from selenium import webdriver
import selenium.common.exceptions

driver = webdriver.Chrome()
NAME = 'my_login'
PASS = 'YOU_SHALL_NOT_PASSword123'


def some_same_accounts():
    try:
        for i in range(2):
            driver.get('http://localhost:8080/signup')
            driver.find_element_by_id('username').send_keys(NAME)
            driver.find_element_by_id('password').send_keys(PASS)
            driver.find_element_by_id('password-confirm').send_keys(PASS)
            driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]'
                                         '/div/div/div[2]/form/div[5]/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/article/div[2]')
        return 0
    except selenium.common.exceptions.NoSuchElementException:
        return 1


def registration_without_password():
    try:
        driver.get('http://localhost:8080/signup')
        driver.find_element_by_id('username').send_keys(NAME)
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]'
                                     '/div/div/div[2]/form/div[5]/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/article/div[2]')
        return 0
    except selenium.common.exceptions.NoSuchElementException:
        return 1


def registration_without_login():
    try:
        driver.get('http://localhost:8080/signup')
        driver.find_element_by_id('password').send_keys(PASS)
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]'
                                     '/div/div/div[2]/form/div[5]/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/article/div[2]')
        return 0
    except selenium.common.exceptions.NoSuchElementException:
        return 1


def registration_without_confirm_password():
    try:
        driver.get('http://localhost:8080/signup')
        driver.find_element_by_id('username').send_keys(NAME)
        driver.find_element_by_id('password').send_keys(PASS)
        driver.find_element_by_id('password-confirm').send_keys(PASS)
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]'
                                     '/div/div/div[2]/form/div[5]/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/article/div[2]')
        return 0
    except selenium.common.exceptions.NoSuchElementException:
        return 1


def registration_with_bad_login():
    try:
        driver.get('http://localhost:8080/signup')
        driver.find_element_by_id('username').send_keys("q")
        driver.find_element_by_id('password').send_keys(PASS)
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]'
                                     '/div/div/div[2]/form/div[5]/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/article/div[2]')
        return 0
    except selenium.common.exceptions.NoSuchElementException:
        return 1


def registration_with_bad_password():
    try:
        driver.get('http://localhost:8080/signup')
        driver.find_element_by_id('username').send_keys(NAME)
        driver.find_element_by_id('password').send_keys(" ")
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]'
                                     '/div/div/div[2]/form/div[5]/div[2]/div/div').click()
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/article/div[2]')
        return 0
    except selenium.common.exceptions.NoSuchElementException:
        return 1


print("1 - система прошла тест, 0 - система не прошла тест")
print("Тестирование системы...")
print(f"Регистрация одинаковых аккаунтов     - {some_same_accounts()}")
print(f"Регистрация без пароля               - {registration_without_password()}")
print(f"Регистрация без логина               - {registration_without_login()}")
print(f"Регистрация с неправильным логином   - {registration_with_bad_login()}")
print(f"Регистрация с неправильным паролем   - {registration_with_bad_password()}")
print(f"Регистрация без подтверждения пароля - {registration_without_confirm_password()}")
