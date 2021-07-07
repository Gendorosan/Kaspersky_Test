from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost:8080/books')
count_of_books = len(driver.find_elements_by_class_name('media'))


def correct_isbn_13():
    driver.get('http://localhost:8080/books')
    incorrect_book_id = []
    for i in range(count_of_books):
        isbn = driver.find_element_by_xpath(f'//*[@id="app"]/section/article[{i + 1}]/figure/p[2]').text[9:]
        try:
            int(isbn[:3])
        except ValueError:
            incorrect_book_id.append(i + 1)
        if isbn[3] != '-':
            incorrect_book_id.append(i + 1)
        try:
            int(isbn[4:])
        except ValueError:
            incorrect_book_id.append(i + 1)
    if len(incorrect_book_id) > 0:
        return 0, incorrect_book_id
    else:
        return 1


def correct_isbn_10():
    incorrect_book_id = []
    driver.get('http://localhost:8080/books')
    for i in range(count_of_books):
        isbn = driver.find_element_by_xpath(f'//*[@id="app"]/section/article[{i + 1}]/figure/p[3]').text[9:]
        try:
            int(isbn)
        except ValueError:
            incorrect_book_id.append(i + 1)

    if len(incorrect_book_id) > 0:
        return 0, incorrect_book_id
    else:
        return 1


def correct_current_price():
    incorrect_book_id = []
    driver.get('http://localhost:8080/books')
    for i in range(count_of_books):
        price = driver.find_element_by_xpath(f'//*[@id="app"]/section/article[{i + 1}]/div[2]/div/div[1]/p[1]').text[
                :-2]
        try:
            float(price)
        except ValueError:
            incorrect_book_id.append(i + 1)
        if float(price) <= 0.0:
            incorrect_book_id.append(i + 1)

    if len(incorrect_book_id) > 0:
        return 0, incorrect_book_id
    else:
        return 1


def correct_previous_price():
    incorrect_book_id = []
    driver.get('http://localhost:8080/books')
    for i in range(count_of_books):
        price = driver.find_element_by_xpath(f'//*[@id="app"]/section/article[{i + 1}]/div[2]/div/div[1]/p[2]').text[
                13:-2]
        try:
            float(price)
        except ValueError:
            incorrect_book_id.append(i + 1)
        if float(price) <= 0.0:
            incorrect_book_id.append(i + 1)

    if len(incorrect_book_id) > 0:
        return 0, incorrect_book_id
    else:
        return 1


def name_is_displayed():
    incorrect_book_id = []
    driver.get('http://localhost:8080/books')
    for i in range(count_of_books):
        name = driver.find_element_by_xpath(f'//*[@id="app"]/section/article[{i + 1}]/div[1]/div/h2').text
        if len(name) == 0:
            incorrect_book_id.append(i + 1)
    if len(incorrect_book_id) > 0:
        return 0, incorrect_book_id
    else:
        return 1


def author_is_displayed():
    incorrect_book_id = []
    driver.get('http://localhost:8080/books')
    for i in range(count_of_books):
        author = driver.find_element_by_xpath(f'//*[@id="app"]/section/article[{i + 1}]/div[1]/div/p[1]').text
        if len(author) == 0:
            incorrect_book_id.append(i + 1)
    if len(incorrect_book_id) > 0:
        return 0, incorrect_book_id
    else:
        return 1


def rating_is_displayed():
    incorrect_book_id = []
    driver.get('http://localhost:8080/books')
    for i in range(count_of_books):
        if driver.find_element_by_xpath(f'//*[@id="app"]/section/article[{i + 1}]/div[1]'
                                        f'/div/div/div/div[1]/img').is_displayed():
            continue
        else:
            incorrect_book_id.append(i + 1)
    if len(incorrect_book_id) > 0:
        return 0, incorrect_book_id
    else:
        return 1


def summary_is_displayed():
    incorrect_book_id = []
    driver.get('http://localhost:8080/books')
    for i in range(count_of_books):
        summary = driver.find_element_by_xpath(f'//*[@id="app"]/section/article[{i + 1}]/div[1]/div/p[2]').text
        if len(summary) == 0:
            incorrect_book_id.append(i + 1)
    if len(incorrect_book_id) > 0:
        return 0, incorrect_book_id
    else:
        return 1


def add_to_basket_is_displayed():
    incorrect_book_id = []
    driver.get('http://localhost:8080/books')
    for i in range(count_of_books):
        if driver.find_element_by_xpath(f'//*[@id="app"]/section/article[{i + 1}]'
                                        f'/div[2]/div/div[2]/div/a').is_displayed():
            continue
        else:
            incorrect_book_id.append(i + 1)
    if len(incorrect_book_id) > 0:
        return 0, incorrect_book_id
    else:
        return 1


def add_book_to_cart():
    driver.get('http://localhost:8080/login')
    driver.find_element_by_id('username').send_keys('qwerty')
    driver.find_element_by_id('password').send_keys('qwerty')
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    names_books_page = []
    names_cart_page = []
    driver.get('http://localhost:8080/books')
    for i in range(count_of_books):
        driver.find_element_by_xpath(f'//*[@id="app"]/section/article[{i + 1}]/div[2]/div/div[2]/div/a').click()
        names_books_page.append(driver.find_element_by_xpath(f'//*[@id="app"]/'
                                                             f'section/article[{i + 1}]/div[1]/div/h2').text)
    driver.get('http://localhost:8080/cart')
    count_of_books_cart_page = len(driver.find_elements_by_class_name('media'))
    for i in range(count_of_books_cart_page):
        names_cart_page.append(driver.find_element_by_xpath(f'//*[@id="app"]/section/div/div[1]/'
                                                            f'article[{i + 1}]/div[1]/div/h2').text)
    if names_cart_page == names_books_page:
        return 1
    else:
        return 0, [book for book in names_books_page if book not in names_cart_page]


print("1 - система прошла тест, 0 - система не прошла тест")
print("Тестирование системы...")
first_test_result = name_is_displayed()
print(f"У всех книг указано название                   - "
      f"{1 if first_test_result == 1 else f'0,    номера книг без название - {first_test_result[1]} '}")
second_test_result = author_is_displayed()
print(f"У всех книг указан автор                       - "
      f"{1 if second_test_result == 1 else f'0,  номера книг без автора - {second_test_result[1]} '}")
third_test_result = rating_is_displayed()
print(f"У всех книг указан рейтинг                     - "
      f"{1 if third_test_result == 1 else f'0,  номера книг без рейтинга - {third_test_result[1]} '}")
fourth_test_result = summary_is_displayed()
print(f"У всех книг указано описание                   - "
      f"{1 if fourth_test_result == 1 else f'0, номера книг без описания - {fourth_test_result[1]} '}")
fifth_test_result = correct_isbn_13()
print(f"У всех книг ISBN-13 указан верно               - "
      f"{1 if fifth_test_result == 1 else f'0, номера книг с неккоректным ISBN-13 - {fifth_test_result[1]} '}")
sixth_test_result = correct_isbn_10()
print(f"У всех книг ISBN-10 указан верно               - "
      f"{1 if sixth_test_result == 1 else f'0, номера книг с неккоректным ISBN-10 - {sixth_test_result[1]} '}")
seventh_test_result = correct_current_price()
print(f"У всех книг текущая цена указана верно         - "
      f"{1 if seventh_test_result == 1 else f'0, номера книг с неккоректной ценой - {seventh_test_result[1]} '}")
eight_test_result = correct_previous_price()
print(f"У всех книг предыдущая цена указана верно      - "
      f"{1 if eight_test_result == 1 else f'0, номера книг с неккоректной ценой - {eight_test_result[1]} '}")
ninth_test_result = add_to_basket_is_displayed()
print(f"У всех книг есть кнопка добавить в корзину     - "
      f"{1 if ninth_test_result == 1 else f'0, номера книг без кнопки - {ninth_test_result[1]}'}")
tenth_test_result = add_book_to_cart()
print(f"У всех книг работает кнопка добавить в корзину - "
      f"{1 if tenth_test_result == 1 else f'0, название книг с нерабочей кнопкой - {tenth_test_result[1]}'}")
