# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные.

import sys, json

def parsing(path_to_file, symbol):
    with open(path_to_file, encoding='utf-8') as f:
        file_data = f.read()
        data_list = []
        for line in file_data.split('\n'):
            data_list.append(line.replace(',', symbol))
    return data_list

fio_list = parsing('data\FIO.txt', ' ')

hobby_list = parsing('data\hobby.txt', ', ')

total_dict = {}

for i in range(len(fio_list)):
    if i >= len(hobby_list):
        total_dict[fio_list[i]] = None
    elif i < len(hobby_list) - 1:
        total_dict[fio_list[i]] = hobby_list[i]
        if i == len(fio_list) - 1:
            with open('data\FIO_hobby.txt', 'w', encoding='utf-8') as f:
                f.write(json.dumps(total_dict))
            with open('data\FIO_hobby.txt', encoding='utf-8') as f:
                check_dict = json.load(f)
                print(check_dict)

            sys.exit(1)
    else:
        total_dict[fio_list[i]] = hobby_list[i]

with open('data\FIO_hobby.txt', 'w', encoding='utf-8') as f:
    json.dump(total_dict, f)

with open('data\FIO_hobby.txt', encoding='utf-8') as f:
    check_dict = json.load(f)
    print(check_dict)
