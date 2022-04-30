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
    day, month, year = map(int, actual_date)
    print(f'Курс {char_code} {rub} рублей, дата: {datetime(day=day, month=month, year=year)}')