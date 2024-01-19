import pytest
from clients.api_client import ApiClient
from path.path_api import ApiPath
from test_data import generate_random_string


@pytest.fixture()
def creating_new_user():

    login_pass =[]
    # генерируем емаил, пароль и имя пользователя
    email = f'{generate_random_string(5)}@mail.ru'
    password = generate_random_string(6)
    name = generate_random_string(6)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на создание пользователя
    api = ApiClient()
    response = api.post(path=ApiPath.path_create_user,
                        payload=payload)

    login_pass.append(email)
    login_pass.append(password)
    login_pass.append(name)

    yield [login_pass, response]

    api.delete(path=f'{ApiPath.path_get_user}',
               headers=response.json()['accessToken'])
