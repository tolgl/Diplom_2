import allure

from clients.api_client import ApiClient
from path.path_api import ApiPath
from test_data import generate_random_string


class TestChangeDataUser:

    @allure.title('Проверка изменения данных пользователя с авторизацией')
    def test_successful_changing_data_user(self, creating_new_user):
        payload = {
            "email": f"new_{generate_random_string(5)}@mail.ru",
            "name": f"new_{generate_random_string(5)}"
        }
        api = ApiClient()
        response = api.patch(path=ApiPath.path_get_user,
                             payload=payload,
                             headers=creating_new_user[1].json()['accessToken'])

        assert response.status_code == 200
        assert response.json()['user']['email'] == payload['email']
        assert response.json()['user']['name'] == payload['name']

    @allure.title('Проверка изменения данных пользователя без авторизации')
    def test_changing_data_user_without_authorization(self, creating_new_user):
        payload = {
            "email": f"new_{generate_random_string(5)}@mail.ru",
            "name": f"new_{generate_random_string(5)}"
        }
        api = ApiClient()
        response = api.patch(path=ApiPath.path_get_user,
                             payload=payload)

        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'
