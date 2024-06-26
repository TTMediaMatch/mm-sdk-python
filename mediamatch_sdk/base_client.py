import requests


class BaseClient:
    def __init__(self, access_token=None):
        self.base_url = "https://mediamatch.tiktok.com"
        self.session = requests.Session()
        if access_token:
            self.access_token = access_token
            self.session.headers.update({"Authorization": f"Bearer {access_token}"})

    def _get(self, path, **kwargs):
        return self.session.get(f"{self.base_url}/{path}", **kwargs)

    def _post(self, path, data=None, json=None, **kwargs):
        return self.session.post(f"{self.base_url}/{path}", data=data, json=json, **kwargs)

    def _put(self, path, data=None, **kwargs):
        return self.session.put(f"{self.base_url}/{path}", data=data, **kwargs)

    def _delete(self, path, **kwargs):
        return self.session.delete(f"{self.base_url}/{path}", **kwargs)
