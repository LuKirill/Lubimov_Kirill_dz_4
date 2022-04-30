# 4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего
# задания. Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов
# функции currency_rates(). Убедиться, что ничего лишнего не происходит.

from utils import currency_rates

currency_rates("usd")
currency_rates("byn")
currency_rates("sgd")