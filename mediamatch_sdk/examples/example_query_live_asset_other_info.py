from mediamatch_sdk.asset.model import ContentCategory
from mediamatch_sdk.client import MediaMatchSDKClient

import json

def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_ee1a59258ae8c1601a4c0eb5f2da66b0f63fcb8c5ec91a451ad544b37677be91"
    client_secret = "caa970543a82aaa7eeeadf85f62c57146f6f2c0dfee8f65570e11aaaa3824a91"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    # STEP 2: Retrieve asset relevant information:
    # asset's creation time, content category, source, status (active, inactive, needs review),
    # recent views for the VOD scan (past 7 days total views, 0 views for the live scan,
    # number of matches on the VOD scan, number of matches on the live scan,
    # reference overlaps & the other RH's names with overlaps.
    try:
        # Option 1: get live other_info with asset_id
        asset_other_info = sdk_client.live_asset_service.get_live_asset_other_info(asset_id=7277926702888583000)
        print("get live other_info with asset_id")
        print(json.dumps(asset_other_info))

        # Option 2: query live other_info page by page
        other_info_list = sdk_client.live_asset_service.query_live_asset_other_info(page=10, pageSize=20)
        print("query live other_info with page and pageSize")
        print(json.dumps(other_info_list))

        # query live other_info with filtered contentCategories and tags
        filtered_other_info_list = sdk_client.live_asset_service.query_live_asset_other_info(
            page=1, pageSize=20,
            contentCategories=[ContentCategory.tv, ContentCategory.sports]
        )
        print("query live other_info with filters page by page")
        print(json.dumps(filtered_other_info_list))

        # Option 3: retrieve all the asset other_info with sdk
        asset_other_info_all = sdk_client.live_asset_service.retrieve_all_asset_other_info()
        print("retrieve all the asset other_info, count=", len(asset_other_info_all))
        print("sample data for the whole asset other_info, data=", json.dumps(asset_other_info_all[:20]))

        # You could also retrieve all the asset metadata with some filters
        asset_other_info_all = sdk_client.live_asset_service.retrieve_all_asset_other_info(
            contentCategories=[ContentCategory.tv, ContentCategory.sports],
        )
        print("retrieve all the asset other_info with filters, count=", len(asset_other_info_all))
        print("sample data for the whole asset other_info, data=", json.dumps(asset_other_info_all[:20]))
    except Exception as e:
        print(f"An error occurred getting the other information of this asset: {e}")


if __name__ == "__main__":
    main()
