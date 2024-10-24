from mediamatch_sdk.base_client import BaseClient
from mediamatch_sdk.util.util import extract_error_message


class UsagePolicy(BaseClient):
    def __init__(self, access_token):
        super().__init__(access_token)

    def retrieve_all_policy(self):
        response = self._get(path=f"/openapi/policy/v1/usage_policy/all")
        if response.status_code == 200:
            return response.json()
        else:
            error_msg = extract_error_message(response)
            raise Exception(f"Failed to retrieve usage policy.\nError Message: {error_msg}")
