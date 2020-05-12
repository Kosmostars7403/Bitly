# Обрезка ссылок с помощью Битли

Скрипт позволяет сократить ссылку с помощью API сервиса [bit.ly](https://bit.ly)

#Как установить

Вам требуется зарегистрироваться на сервисе [bit.ly](https://bit.ly) и получить ключ API.
GENERIC ACCESS TOKEN — нужный тип токена. Пример - `17c09e20ad155405123ac1977542fecf00231da7`. Затем запишите ключ в значение переменной `BITLY_TOKEN`
в файле `.env`.

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:

`
pip install -r requirements.txt
`

###Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://devman.org).