# Простой калькулятор на FLASK

## Как работает?

используя http запросы мы можем реализовать взаимодействие с сервером.
В данном проекте участвую два запроса: POST и GET.

**POST** - получает данные на сервер и их обрабатывает \
**GET** - получает данные из сервера и показывает их пользователю.

В программе мы вписываем 3 значения: 2 цифры и знак.
Они по запросу **POST** отправляются на сервер, где и уже произойдет соотвествущая операция. Потом сервер высылает на сайт **GET** запрос с результатом нашего вычисления.