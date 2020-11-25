import ctypes
import matplotlib.pyplot as plt
import os

# Корневая директория проекта
ROOT = 'dll/'

# Имена файлов с библиотеками
DLLS = [
    'Lib.dll',
    'Lib2-2-1.dll',
    'Lib2-2-2.dll',
    'Lib2-2-3.dll',
    'Lib2-2-3-1.dll',
    'Lib2-2-3-2.dll',
    'MyDLL.dll',
]


def is_dll_work(_item):
    """
    Функция проверяет возможность загрузки DLL библиотек
    :param _item: имя файла dll библиотеки
    :return: true/false
    """
    try:
        ctypes.CDLL(os.path.join(ROOT, _item))
    except OSError:
        print(f'Библиотеку {_item} загрузить не удалось')
        return False
    else:
        print(f'Библиотека {_item} успешно загружена')
        return True


def make_dll_connection(_item):
    """
    Функция загружает отобранные dll библиотеки
    :param _item: имя файла dll библиотеки
    :return: загруженная dll библиотека
    """
    return ctypes.CDLL(os.path.join(ROOT, _item))


def make_data_for_graphic(_item):
    """
    Функция проверяет имеет ли dll необходитмые функции и подготавливает данные для внесения на график
    :param _item: dll библиотека
    """
    try:
        func_name = _item.FuncName
        the_func = _item.TheFunc
    except AttributeError:
        print('Функция в данной библиотеке повреждена')
        return

    func_name.restype = ctypes.c_char_p

    the_func.argtype = ctypes.c_double
    the_func.restype = ctypes.c_double

    name = func_name().decode('ascii')

    x, y = [], []

    for _i in range(11):
        x.append(_i)
        y.append(the_func(ctypes.c_double(_i)))

    draw_graphic(x, y, name)


def draw_graphic(x, y, name):
    """
    Функция строит график
    :param x: входной список значений оси X
    :param y: входной список значений оси Y
    :param name: математическая функция
    """
    plt.figure(figsize=(15, 8))
    plt.plot(x, y)
    plt.xticks(x)
    plt.yticks(y)
    plt.ylable = 'Ось Y'
    plt.title(name)
    plt.show()


if __name__ == '__main__':
    print('Начинаем загрузку библиотек')
    active_dll_list = list(filter(is_dll_work, DLLS))
    print('Процесс загрузки библиотек завершен')

    make_dll_connection_list = list(map(make_dll_connection, active_dll_list))

    while True:
        print('Пожалуйста, выберете для какой библиотеки просчитать функцию:')
        for i, item in enumerate(active_dll_list):
            print(f'\t{i+1}.) {item};')
        print('\tДля выхода нажмите любую другую кнопку...')
        choise = int(input())
        if choise in [1, 2, 3, 4, 5, 6]:
            make_data_for_graphic(make_dll_connection_list[choise-1])
        else:
            break
