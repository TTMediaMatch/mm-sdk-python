from mediamatch_sdk.client import MediaMatchSDKClient
import json, sys


def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_ee1a59258ae8c1601a4c0eb5f2da66b0f63fcb8c5ec91a451ad544b37677be91"
    client_secret = "caa970543a82aaa7eeeadf85f62c57146f6f2c0dfee8f65570e11aaaa3824a91"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    # STEP 2: Retrieve all the usage policy
    try:
        resp = sdk_client.usage_policy_service.retrieve_all_policy()
        print("retrieve all the usage policy, total_count=", resp.get('data').get('total'))
        print(json.dumps(resp))

    except Exception as e:
        print(f"An error occurred getting the metadata of this asset: {e}")


if __name__ == "__main__":
    main()
