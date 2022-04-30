# 3*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
# дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
# как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

import requests
import decimal
from datetime import datetime

def currency_rates(char_code):
    char_code = char_code.upper()
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text

    if char_code not in response:
        return None

    rub = response[response.find("<Value>", response.find(char_code)) + 7:response.find("</Value>", response.find(char_code))].split(",")
    rub = decimal.Decimal(".".join(rub))
    actual_date = response[60:70].split(".")
    """при использовании метода .find аналогично использованию для rub появлялась ошибка
    (invalid literal for int() with base 10: ' version="1')
    при выводе actual_date -> version="1.0" encoding="windows-1251"?><ValCurs Date="16.04.2022
    пришлось отсчитать срез до нужной даты"""
    day, month, year = map(int, actual_date)

    print(f'Курс {char_code} {rub} рублей, дата: {datetime(day = day, month = month, year = year)}')
    print(type(rub))
    print(type(actual_date))

currency_rates("usd")
currency_rates("euR")
currency_rates("GBP")
currency_rates("edf")