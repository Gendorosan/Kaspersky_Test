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


def delete_book():
    driver.get('http://localhost:8080/books')
    driver.find_element_by_xpath(f'//*[@id="app"]/section/article[1]/div[2]/div/div[2]/div/a').click()
    driver.find_element_by_xpath(f'//*[@id="app"]/section/article[2]/div[2]/div/div[2]/div/a').click()
    driver.get('http://localhost:8080/cart')
    count_of_books = len(driver.find_elements_by_class_name('media'))
    driver.find_element_by_xpath('//*[@id="app"]/section/div/div[1]/article[1]/div[1]'
                                 '/div/div/div/div[3]/button').click()
    new_count_of_books = len(driver.find_elements_by_class_name('media'))
    if new_count_of_books == count_of_books:
        return 0, 'книга не удалилась'
    if count_of_books - new_count_of_books > 1:
        return 0, 'удалилось больше одной книги'
    else:
        return 1


print("1 - система прошла тест, 0 - система не прошла тест")
print("Тестирование системы...")
first_test_result = check_price()
print(f"Цена книг соответсвует стоимости заказа          - {first_test_result}")
second_test_result = count_update()
print(f"Количество книг в корзине корректно обновляется  - {second_test_result}")
third_test_result = delete_book()
print(f"Книга корректно удаляется из корзины             - "
      f"{1 if third_test_result == 1 else f'0, {third_test_result[1]}'}")
