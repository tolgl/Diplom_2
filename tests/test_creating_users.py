import allure
import pytest

from clients.api_client import ApiClient
from path.path_api import ApiPath


class TestCreateUser:

    @allure.title('Проверка создания уникального пользователя')
    def test_successful_create_user_unique_data(self, creating_new_user):

        assert creating_new_user[1].status_code == 200
        assert creating_new_user[1].json()['accessToken'] != ''

    @allure.title('Проверка повторного создания существующего пользователя')
    def test_create_user_with_same_data(self, creating_new_user):

        payload = {
            "email": creating_new_user[0][0],
            "password": creating_new_user[0][1],
            "name": creating_new_user[0][2]
        }

        api = ApiClient()
        response = api.post(path=ApiPath.path_create_user,
                            payload=payload)

        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'

    @allure.title('Проверка создания пользователя без одного из полей')
    @pytest.mark.parametrize('email,password,name',
                             [
                                 ['test@test.ru', '12345678', ''],
                                 ['test@test.ru', '', 'test'],
                                 ['', '12345678', 'test'],
                                 ['', '', '']
                             ])
    def test_create_user_with_blank_fields(self, creating_new_user, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        api = ApiClient()
        response = api.post(path=ApiPath.path_create_user,
                            payload=payload)

        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'
