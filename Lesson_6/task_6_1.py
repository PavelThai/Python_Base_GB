#1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>)

with open('data/nginx_logs.txt', encoding='utf-8') as log_file:
    list_info = []
    for line in log_file:
        remote_addr = line.split(' ')[0]
        requested_type = line.split('"')[1].split(' ')[0]
        requested_resource = line.split('"')[1].split(' ')[1]
        list_info.append((remote_addr, requested_type, requested_resource))
print(list_info)