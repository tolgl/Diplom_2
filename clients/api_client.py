import json
import requests
from config import BASE_URL


class ApiClient:
    def __init__(self):
        self.base_url = BASE_URL

    def post(self, path, payload, headers=None):
        response_post = requests.post(url=self.base_url + path,
                                      data=json.dumps(payload),
                                      headers={"Content-type": "application/json", "Authorization": headers})
        return response_post

    def get(self, path, get_params=None, headers=None):
        response_get = requests.get(url=self.base_url + path,
                                    params=get_params,
                                    headers={"Authorization": headers})

        return response_get

    def delete(self, path, get_params=None, headers=None):
        response_delete = requests.get(url=self.base_url + path,
                                       params=get_params,
                                       headers={"Content-type": "application/json", "Authorization": headers})

        return response_delete

    def patch(self, path, payload, headers=None):
        response_patch = requests.patch(url=self.base_url + path,
                                        data=json.dumps(payload),
                                        headers={"Content-type": "application/json", "Authorization": headers})

        return response_patch

