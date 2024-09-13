import time

from mediamatch_sdk.client import MediaMatchSDKClient

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_8eea5fd6c584ab440ffc71f27da395b1c415dceea6e1bdac522002b04f71bf67"
    client_secret = "4ae0fb00293ac805f52ab4021c432d7f5acf75bba964a72114987de0818eeb6e"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    batch_id = 7410872219431337990
    # STEP 2: Check the delivery status, this can take up to an hour until it become success
    try:
        delivery_status = sdk_client.live_upload_service.get_delivery_status(batch_id)
        print(delivery_status)
    except Exception as e:
        print(f"An error occurred querying delivery status: {e}")

if __name__ == "__main__":
    main()
