import allure

from clients.api_client import ApiClient
from path.path_api import ApiPath


class TestCreateUser:

    @allure.title('Получение заказа авторизованного пользователя')
    def test_get_list_orders_authorized_user(self, creating_new_user, get_id_ingredients):
        payload = {
            "ingredients": get_id_ingredients
        }
        api = ApiClient()
        # создаем пользователю заказ
        api.post(path=ApiPath.path_order,
                 payload=payload,
                 headers=creating_new_user[1].json()['accessToken'])
        # получаем заказы пользователя
        response = api.get(path=ApiPath.path_order,
                           headers=creating_new_user[1].json()['accessToken'])

        assert response.status_code == 200
        assert len(response.json()['orders']) != 0

    @allure.title('Получение заказа неавторизованного пользователя')
    def test_get_list_orders_non_authorized_user(self):
        api = ApiClient()
        response = api.get(path=ApiPath.path_order)

        assert response.status_code == 401
        assert response.json()['message'] == 'You should be authorised'
