# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests. В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
# str, решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
# выведите курсы доллара и евро.

import requests
import decimal
def currency_rates(char_code):
    char_code = char_code.upper()
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text

    if char_code not in response:
        return None

    rub = response[response.find("<Value>", response.find(char_code)) + 7:response.find("</Value>", response.find(char_code))].split(",")
    rub = decimal.Decimal(".".join(rub))
    print(rub)
    print(type(rub))
#
# currency_rates("usd")
# currency_rates("euR")
# currency_rates("GBP")
# currency_rates("edf")


