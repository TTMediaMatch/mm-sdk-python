from mediamatch_sdk.client import MediaMatchSDKClient

def main():

    # Initialize the SDK by

    # option 1: if you have set environment variables (MM_CLIENT_ID, MM_CLIENT_SECRET)
    # sdk_client = MediaMatchSDKClient()

    # option 2: pass in them explicitly

    client_id = "cli_fcf0a39c9d04e22bdccf5c8f7e4b94c271f38aede738d01523ad101643ab8e7e"
    client_secret = "7a0388a17b3e75139fda645be6f052467a4781a71b6c22a006415803a050ffc9"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    # now you should see the access_token
    print(sdk_client.access_token)

if __name__ == "__main__":
    main()
