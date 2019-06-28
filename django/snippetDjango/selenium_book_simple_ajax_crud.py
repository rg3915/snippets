import time
from gen_random_values import gen_book, gen_date, convert_date, gen_digits, gen_decimal
from selenium import webdriver


# page = webdriver.Firefox()
page = webdriver.Chrome(
    executable_path='/home/rg3915/chromedriver/chromedriver')
page.maximize_window()
time.sleep(0.5)
page.get('http://localhost:8000/books/')

search = page.find_element_by_class_name('btn-primary')
search.click()
time.sleep(0.5)

# title
# author
# publication_date
# pages
# price
# book_type

fields = [
    ['id_title', gen_book()['title']],
    ['id_author', gen_book()['author']],
    ['id_publication_date', convert_date(gen_date())],
    ['id_pages', gen_digits(4)],
    ['id_price', gen_decimal(5, 2)],
]

# driver.find_element_by_css_selector('.modal-footer > button[data-dismiss="modal"]')

for field in fields:
    search = page.find_element_by_css_selector(
        '.modal-book > id_title')  # field[0])
    search.send_keys(field[1])
    time.sleep(0.2)


# button = page.find_element_by_id('id_submit')
# button = page.find_element_by_class_name('btn-primary')
# button.click()

# page.quit()
