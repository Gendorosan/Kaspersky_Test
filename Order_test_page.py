from datetime import datetime
from selenium import webdriver
import selenium.common.exceptions

driver = webdriver.Chrome()
driver.get('http://localhost:8080/login')
driver.find_element_by_id('username').send_keys('qwerty')
driver.find_element_by_id('password').send_keys('qwerty')
driver.find_element_by_xpath('//*[@id="submit"]').click()
driver.find_element_by_xpath('//*[@id="app"]/section/article[1]/div[2]/div/div[2]/div/a').click()
driver.get('http://localhost:8080/cart')

try:
    driver.find_element_by_xpath('//*[@id="app"]/nav/div[2]/div[2]/div[2]/div/a')
    driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/form/div/div[2]/button').click()
except selenium.common.exceptions.NoSuchElementException:
    driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/div/div[2]/'
                                 'div[2]/form/div[3]/div[1]/div/div/a').click()
    driver.find_element_by_id('name').send_keys('TestOrderPage')
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
    driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/form/div/div[2]/button').click()


def order_number_is_correct():
    number = driver.find_element_by_xpath('//*[@id="app"]/section/h1').text[7:]
    try:
        if int(number) > 0:
            return 1
    except ValueError:
        if number > '':
            return 1
    return 0


def order_number_is_unique():
    numbers = []
    for i in range(10):
        driver.get('http://localhost:8080/cart')
        driver.find_element_by_xpath('//*[@id="app"]/section/div/div[2]/form/div/div[2]/button').click()
        number = driver.find_element_by_xpath('//*[@id="app"]/section/h1').text[7:]
        if number not in numbers:
            numbers.append(number)
    return 1 if len(numbers) == 10 else 0


def delivery_date():
    date = driver.find_element_by_xpath('//*[@id="app"]/section/div/p[2]/span').text
    try:
        datetime.today().date().replace(day=int(date[:2]), month=int(date[3:-5]), year=int(date[6:]))
        return 1
    except ValueError:
        return 0


def date_of_execution():
    date = driver.find_element_by_xpath('//*[@id="app"]/section/div/p[1]').text[15:]
    try:
        datetime.today().replace(day=int(date[:2]), month=int(date[3:-15]), year=int(date[6:-9]), hour=date[11:-7],
                                 minute=date[14:-4], second=date[17:-1])
        return 1
    except ValueError:
        return 0


def check_count():
    rows_count = driver.execute_script("return document.getElementsByTagName('tr').length") - 2
    count_of_books = 0
    for i in range(rows_count):
        count_of_books += int(driver.find_element_by_xpath(f'//*[@id="app"]/section/'
                                                           f'div/table/tbody/tr[{i + 1}]/td[2]').text)
    actual_count = int(driver.find_element_by_xpath('//*[@id="app"]/section/div/table/tfoot/tr/th[3]').text)
    return 1 if count_of_books == actual_count else 0


def check_price():
    rows_count = driver.execute_script("return document.getElementsByTagName('tr').length") - 2
    total_price = 0
    for i in range(rows_count):
        total_price += float(driver.find_element_by_xpath(f'//*[@id="app"]/section/'
                                                          f'div/table/tbody/tr[{i + 1}]/td[3]').text) * \
                       float(driver.find_element_by_xpath(f'//*[@id="app"]/section/'
                                                          f'div/table/tbody/tr[{i + 1}]/td[2]').text)
    actual_price = float(driver.find_element_by_xpath('//*[@id="app"]/section/div/table/tfoot/tr/th[4]').text[:-2])
    return 1 if total_price == actual_price else 0


print("1 - система прошла тест, 0 - система не прошла тест")
print("Тестирование системы...")
print(f"Корректный номер заказа             - {order_number_is_correct()}")
print(f"Уникальный номер заказа             - {order_number_is_unique()}")
print(f"Корректная дата доставки            - {delivery_date()}")
print(f"Корректная дата оформления          - {date_of_execution()}")
print(f"Количество книг совпадает с 'итого' - {check_count()}")
print(f"Стоимость книг совпадает с 'итого'  - {check_price()}")
