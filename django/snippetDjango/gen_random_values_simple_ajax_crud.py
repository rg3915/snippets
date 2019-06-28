import csv
import string
from random import random, randint, choice
from datetime import date, datetime, timedelta
from decimal import Decimal


book_list = []


''' Lendo os dados de books.csv '''
with open('csv/books.csv', 'r') as f:
    items = csv.DictReader(f)
    for item in items:
        book_list.append(item)
    f.close


def gen_book():
    idx = randint(0, len(book_list))
    d = {}
    d['title'] = book_list[idx]['name']
    d['author'] = book_list[idx]['authors']
    return d


def gen_date(min_year=1900, max_year=datetime.now().year):
    # gera um date no formato yyyy-mm-dd
    start = date(min_year, 1, 1)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random()


def convert_date(d):
    # converte data no formato mês, dia, ano.
    return d.strftime('%m/%d/%Y')


def gen_digits(max_length):
    return str(''.join(choice(string.digits) for i in range(max_length)))


def gen_decimal(max_digits=5, decimal_places=2):
    num_as_str = lambda x: ''.join([str(randint(0, 9)) for i in range(x)])
    return Decimal("%s.%s" % (num_as_str(max_digits - decimal_places), num_as_str(decimal_places)))
gen_decimal.required = ['max_digits', 'decimal_places']
