import time
import json, sys

from mediamatch_sdk.client import MediaMatchSDKClient
from mediamatch_sdk.asset.model import ContentCategory

def main():
    # STEP 1: Initialize the SDK

    client_id = "cli_ee1a59258ae8c1601a4c0eb5f2da66b0f63fcb8c5ec91a451ad544b37677be91"
    client_secret = "caa970543a82aaa7eeeadf85f62c57146f6f2c0dfee8f65570e11aaaa3824a91"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    # STEP 2: Retrieve metadata
    try:
        # Option 1: get video metadata with asset_id
        metadata = sdk_client.video_asset_service.get_video_asset_metadata(asset_id=7277926702888583000)
        print("get video metadata with asset_id")
        print(json.dumps(metadata))

        # Option 2: query video metadata page by page
        metadata_list = sdk_client.video_asset_service.query_video_asset_metadata(page=10, pageSize=20)
        print("query video metadata with page and pageSize")
        print(json.dumps(metadata_list))

        # query video metadata with filtered contentCategories and tags
        filtered_metadata_list = sdk_client.video_asset_service.query_video_asset_metadata(
            page=1, pageSize=20,
            contentCategories=[ContentCategory.tv, ContentCategory.sports],
            tags=['entretenimento']
        )
        print("query video metadata with filters page by page")
        print(json.dumps(filtered_metadata_list))

        # Option 3: retrieve all the asset metadata with sdk
        asset_metadata_all = sdk_client.video_asset_service.retrieve_all_asset_metadata()
        print("retrieve all the asset metadata, count=", len(asset_metadata_all))
        print("sample data for the whole asset metadata, data=", json.dumps(asset_metadata_all[:20]))

        # You could also retrieve all the asset metadata with some filters
        filtered_asset_metadata_all = sdk_client.video_asset_service.retrieve_all_asset_metadata(
            contentCategories=[ContentCategory.tv, ContentCategory.sports],
            tags=['entretenimento']
        )
        print("retrieve all the asset metadata with filters, count=", len(filtered_asset_metadata_all))
        print("sample data for the whole asset metadata, data=", json.dumps(filtered_asset_metadata_all[:20]))

    except Exception as e:
        print(f"An error occurred getting the metadata of this asset: {e}")


if __name__ == "__main__":
    main()
