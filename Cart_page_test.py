from selenium import webdriver
import selenium.common.exceptions

"""
 В требованиях к сайту указано, что пароль должен содержать цифру, однако сайт не даёт авторизоваться в существующем
 аккаунте в пароле которого содержится цифра. Поэтому логин и пароль - qwerty
 
 Перед тем как начать работу с данной страницей необходимо авторизироваться и добавить товар в корзину
"""
driver = webdriver.Chrome()
driver.get('http://localhost:8080/login')
driver.find_element_by_id('username').send_keys('qwerty')
driver.find_element_by_id('password').send_keys('qwerty')
driver.find_element_by_xpath('//*[@id="submit"]').click()
driver.find_element_by_xpath('//*[@id="app"]/section/article[1]/div[2]/div/div[2]/div/a').click()
driver.get('http://localhost:8080/cart')

try:
    driver.find_element_by_xpath('//*[@id="app"]/nav/div[2]/div[2]/div[2]/div/a')
except selenium.common.exceptions.NoSuchElementException:
    driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div[2]/'
                                 'div[2]/form/div[3]/div[1]/div/div/a').click()
    driver.find_element_by_id('name').send_keys('TestCartPage')
    driver.find_element_by_id('username').send_keys('qwerty')
    driver.find_element_by_id('password').send_keys('qwerty')
    driver.find_element_by_id('password-confirm').send_keys('qwerty')
    driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div/div[2]'
                                 '/form/div[5]/div[2]/div/div/button').click()
    driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/article/div[2]/a').click()
    driver.find_element_by_id('username').send_keys('qwerty')
    driver.find_element_by_id('password').send_keys('qwerty')
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    driver.find_element_by_xpath('//*[@id="app"]/section/article[1]/div[2]/div/div[2]/div/a').click()
    driver.find_element_by_xpath('//*[@id="app"]/nav/div[2]/div[2]/div[2]/div/a').click()
    driver.find_element_by_xpath('//*[@id="app"]/section/article[1]/div[2]/div/div[2]/div/a').click()
    driver.get('http://localhost:8080/cart')


def check_price():
    price = float(driver.find_element_by_xpath('//*[@id="app"]/section/div/div[1]/article/div[2]/p/strong').text[:-2])
    count = float(driver.find_element_by_xpath('//*[@id="input"]').get_attribute('value'))
    total_price = price * count
    actual_price = float(driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/'
                                                      'form/div/div[1]/p/strong').text[:-2])
    if total_price == actual_price:
        return 1
    else:
        return 0


def count_update():
    price = float(driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/'
                                               'form/div/div[1]/p/strong').text[:-2])
    driver.find_element_by_xpath('//*[@id="input"]').send_keys(0)
    new_price = float(driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/'
                                                   'form/div/div[1]/p/strong').text[:-2])
    driver.find_element_by_xpath('//*[@id="app"]/section/div/div[1]/article/div[1]/div/div'
                                 '/div/div[2]/div/button').click()
    if price != new_price:
        return 1
    else:
        return 0




