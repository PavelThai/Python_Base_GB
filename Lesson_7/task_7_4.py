# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }

from os import walk, stat
from os.path import join

path = r'd:'

def rating_file_size(path):

    result_dict = {'100': 0, '1 000': 0, '10 000': 0, '100 000': 0, '>100 000': 0}

    for root, dirs, files in walk(path):
        for file in files:
            file_path = join(root, file)
            if stat(file_path).st_size < 100:
                result_dict['100'] += 1
            elif 100 <= stat(file_path).st_size < 1000:
                result_dict['1 000'] += 1
            elif 1000 <= stat(file_path).st_size < 10000:
                result_dict['10 000'] += 1
            elif 10000 <= stat(file_path).st_size < 100000:
                result_dict['100 000'] += 1
            else:
                result_dict['>100 000'] += 1
    return result_dict

print(rating_file_size(path))