# Автотесты API для сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/)
*В проекте использовалась библиотека Requests и фреймворки Pytest, Allure*


1. Файл tests/conftest.py содержит фикстуры добавления/удаления пользователя и получения списка хэша ингредиента
2. Файл tests/test_login_user.py содержит автотесты логина пользователя:
   - __test_login_existing_user__ - проверяет логин существующего пользователя
   - __test_login_user_with_invalid_email_and_password__ - проверяет логин пользователя с неверным логином и паролем
3. Файл tests/test_creating_users.py содержит автотесты создания пользователя:
   - __test_successful_create_user_unique_data__ - проверяет создание пользователя с уникальными данными
   - __test_create_user_with_same_data__ - проверяет создание уже существующего пользователя
   - __test_create_user_with_blank_fields__ - проверяет создание пользователя с пустыми полями
4. Файл tests/test_changing_data_user.py содержит автотесты изменения пользователя:
   - __test_successful_changing_data_user__ - проверяет изменение данных под авторизованным пользователем
   - __test_changing_data_user_without_authorization__ - проверяет изменение данных под неавторизованным пользователем
5. Файл tests/create_order.py содержит автотесты создания заказа
   - __test_create_order_with_ingredients_and_authorization__ - проверяет создание заказа с указанием ингредиентов и под авторизованным пользователем
   - __test_create_order_with_ingredients_and_non_authorization__ - проверяет создание заказа с указанием ингредиентов и под неавторизованным пользователем
   - __test_create_order_without_ingredients_and_authorization__ - проверяет создание заказа без ингредиентов и под авторизованным пользователем
   - __test_create_order_with_invalid_hash_ingredients__ - проверяет создание заказа с невалидным хэшом ингредиента
6. Файл tests/test_get_orders_user.py содержит автотесты получения заказа у пользователя:
   - __test_get_list_orders_authorized_user__ - проверяет получение заказа под авторизованным пользователем
   - __test_get_list_orders_non_authorized_user__ - проверяет получение заказа под неавторизованным пользователем
7. Файл config.py содержит базовые переменные
8. Файл requirements.txt содержит используемые зависимости в проекте
9. Файл test_data.py содержит генератор тестовых данных