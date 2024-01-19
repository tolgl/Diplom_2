import allure
from clients.api_client import ApiClient
from path.path_api import ApiPath
from test_data import generate_random_string


class TestCreateOrder:

    @allure.title('Проверка создания заказа с авторизацией и ингредиентами')
    def test_create_order_with_ingredients_and_authorization(self, creating_new_user, get_id_ingredients):
        payload = {
            "ingredients": get_id_ingredients
        }
        api = ApiClient()
        response = api.post(path=ApiPath.path_order,
                            payload=payload,
                            headers=creating_new_user[1].json()['accessToken'])

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверка создания заказа без авторизации и с ингредиентами')
    def test_create_order_with_ingredients_and_non_authorization(self, creating_new_user, get_id_ingredients):
        payload = {
            "ingredients": get_id_ingredients
        }
        api = ApiClient()
        response = api.post(path=ApiPath.path_order,
                            payload=payload)

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Проверка создания заказа c авторизацией и без ингредиентов')
    def test_create_order_without_ingredients_and_authorization(self, creating_new_user):
        payload = {
            "ingredients": ""
        }
        api = ApiClient()
        response = api.post(path=ApiPath.path_order,
                            payload=payload,
                            headers=creating_new_user[1].json()['accessToken'])

        assert response.status_code == 400
        assert response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title('Проверка создания заказа c невалидным хэшем ингредиента')
    def test_create_order_with_invalid_hash_ingredients(self, creating_new_user, get_id_ingredients):
        payload = {
            "ingredients": f"{get_id_ingredients}{generate_random_string(5)}"
        }
        api = ApiClient()
        response = api.post(path=ApiPath.path_order,
                            payload=payload,
                            headers=creating_new_user[1].json()['accessToken'])

        assert response.status_code == 500
