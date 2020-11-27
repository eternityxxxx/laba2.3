##### Пользовательская DLL находится в папке dll/MyDLL.dll
##### DLL реализует две функции:
1. FuncName() ->  PAnsiChar (stdcall) 'y=x+2'
2. TheFunc(x: double) -> Double (cdecl)

##### Для проверки:
1. Создать новую директорию под проект и склонировать репозиторий:
```
git clone https://github.com/eternityxxxx/laba2.3.git
```
2. Создать вирутальное окружение:
```
python -m venv venv
```
3. Активировать окружение:
```
cd venv/Scripts activate
```
4. Установить зависимости:
```
pip install -r requirements.txt
```
5. Запустить код:
```
python main.py
```
Либо в лоб установить ctypes и matplotlib глобально на компьютер:
```
pip install ctypes
pip install matplotlib
```
И перейти к шагу 5