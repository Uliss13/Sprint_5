# Sprint_5

Автотесты для сервиса Stellar Burgers.

## Стек

- Python 3.9
- Selenium 4.36
- pytest 8.4
- Google Chrome

## Структура

- `tests/` — тесты
- `conftest.py` — фикстуры
- `locators.py` — локаторы страниц
- `helpers.py` — константы и генератор email
- `requirements.txt` — зависимости
- `README.md` — описание проекта
- `.gitignore` — исключения для git

## Тесты

- `test_registration.py` — регистрация (успешная + ошибка короткого пароля)
- `test_login.py` — вход через 4 точки входа
- `test_profile.py` — переход в личный кабинет и выход
- `test_navigation.py` — переход в конструктор и по логотипу
- `test_constructor.py` — разделы «Булки», «Соусы», «Начинки»

## Запуск

```bash
pip install -r requirements.txt
pytest
```

## Фикстуры

- `driver` — открывает/закрывает браузер
- `registered_user` — регистрирует нового пользователя, отдаёт `(email, password)`
- `authorized_user` — логинит пользователя, отдаёт драйвер

## Генерация email

`helpers.email_generator()` создаёт уникальный email
в формате `имя_фамилия_когорта_3цифры@домен`.

## Локаторы

Описаны в `locators.py` с комментариями:

- `MainPage` — главная
- `LoginPage` — вход
- `RegistrationPage` — регистрация
- `RecoverPage` — восстановление пароля
- `Constructor` — конструктор
- `ProfilePage` — личный кабинет