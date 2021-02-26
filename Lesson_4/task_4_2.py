# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
#
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.

from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

content_char_code = content.split('<CharCode>')
content_char_code.pop(0)

content_value = content.split('<Value>')
content_value.pop(0)

cur_exchange = {}

for i in range(len(content_char_code)):
    value = float(content_value[i].split('<')[0].replace(',', '.'))
    cur_exchange[content_char_code[i][0:3]] = value

def currency_rates(*args, cur_exchange = cur_exchange):
    user_dict = {}
    for el in args:
        user_dict[el.upper()] = cur_exchange.get(el.upper(), 'Нет такой валюты')
    return user_dict

if __name__ == '__main__':
    print(currency_rates('thb', 'eur', 'gbp', 'лорыва'))