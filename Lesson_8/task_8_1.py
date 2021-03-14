#1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.

import re

adr1 = 'someone@geekbrains.ru'
adr2 = 'someone@geekbrainsru'

data = re.compile(r"(?P<username>[\w'.+-]+)@(?P<domain>[a-z0-9.-]+\.[a-z]+)")


def email_parse(template, address):
    if template.search(address) is not None:
        user_dict = dict(*map(lambda x: x.groupdict(), template.finditer(address)))
        return user_dict
    else:
        raise ValueError('Адрес введен с ошибками. Должно быть: user@domain.zone')


print(email_parse(data, adr1))

print(email_parse(data, adr2))
