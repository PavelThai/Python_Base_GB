# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp


from os import mkdir, path
from os.path import join, abspath

main_dir_name = 'my_project'
working_dir_names = ('settings', 'mainapp', 'adminapp', 'authapp')
main_dir_path = abspath(join('.', main_dir_name))
if not path.exists(main_dir_name):
    mkdir(main_dir_name)
for el in working_dir_names:
    if not path.exists(join(main_dir_path, el)):
        mkdir(join(main_dir_path, el))