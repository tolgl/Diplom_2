import allure
import pytest

from clients.api_client import ApiClient
from path.path_api import ApiPath
from test_data import generate_random_string


class TestLoginUser:

    @allure.title('Проверка логина под существующим пользователем')
    def test_login_existing_user(self, creating_new_user):
        payload = {
            "email": creating_new_user[0][0],
            "password": creating_new_user[0][1]
        }
        api = ApiClient()
        response = api.post(path=ApiPath.path_login_user,
                            payload=payload)

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверка логина с неверным логином и паролем')
    @pytest.mark.parametrize('email,password',
                             [
                                 [f'{generate_random_string(7)}@mail.ru', generate_random_string(8)],
                                 ['', generate_random_string(8)],
                                 [f'{generate_random_string(7)}@mail.ru', ''],
                                 ['', '']
                             ])
    def test_login_non_existing_user(self, creating_new_user, email, password):
        payload = {
            "email": email,
            "password": password
        }
        api = ApiClient()
        response = api.post(path=ApiPath.path_login_user,
                            payload=payload)

        assert response.status_code == 401
        assert response.json()['message'] == 'email or password are incorrect'
