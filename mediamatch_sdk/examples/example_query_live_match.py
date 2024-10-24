import time, math
import json

from mediamatch_sdk.asset.model import MatchInfoRetrieve, PolicyAction, DisputeStatus
from mediamatch_sdk.client import MediaMatchSDKClient


def main():
    # STEP 1: Initialize the SDK
    client_id = "cli_ee1a59258ae8c1601a4c0eb5f2da66b0f63fcb8c5ec91a451ad544b37677be91"
    client_secret = "caa970543a82aaa7eeeadf85f62c57146f6f2c0dfee8f65570e11aaaa3824a91"
    sdk_client = MediaMatchSDKClient(client_id, client_secret)

    start_time = 1704067200  # 2024-01-01 00:00:00
    end_time = 1706745600  # 2024-02-01 00:00:00

    # Option1: [Deprecated] use get_live_match to retrieve asset match info
    # Note: retrieve interval can't be greater than one month
    asset_match_info1 = sdk_client.live_asset_service.get_live_match(
        asset_id=7277926702888583000,
        page=1, pageSize=20,
        start_time=start_time, end_time=end_time
    )
    print("[Deprecated] use get_live_match to retrieve asset match info")
    print(json.dumps(asset_match_info1))

    # Option2: use query_live_match to retrieve asset match info
    # Note: retrieve interval can't be greater than one month
    asset_match_retrieve_param = MatchInfoRetrieve(
        start_time=start_time, end_time=end_time,
        page=1, page_size=20,
        asset_id=7277926702888583000,
    )
    asset_match_info2 = sdk_client.live_asset_service.query_live_match(asset_match_retrieve_param)
    print("use query_live_match to retrieve asset match info")
    print(json.dumps(asset_match_info2))

    # You could also retrieve asset match info with some filters
    filtered_asset_match_retrieve_param = MatchInfoRetrieve(
        start_time=start_time, end_time=end_time,
        page=1, page_size=20,
        asset_id=7277926702888583000,
        filtered_policy_action=[PolicyAction.allow],
        filtered_dispute_status=[DisputeStatus.none]
    )
    filtered_asset_match_info = sdk_client.live_asset_service.query_live_match(filtered_asset_match_retrieve_param)
    print("use query_live_match to retrieve asset match info with some filters")
    print(json.dumps(filtered_asset_match_info))

    # Option 3: use query_live_match to retrieve match info without asset_id constraint
    match_retrieve_param = MatchInfoRetrieve(
        start_time=start_time, end_time=end_time,
        page=1, page_size=20,
    )
    match_info = sdk_client.live_asset_service.query_live_match(match_retrieve_param)
    print("use query_live_match to retrieve match info without asset_id constraint")
    print(json.dumps(match_info))

    # You could also retrieve these match info with some filters
    filtered_match_retrieve_param = MatchInfoRetrieve(
        start_time=start_time, end_time=end_time,
        page=1, page_size=20,
        filtered_policy_action=[PolicyAction.allow],
        filtered_dispute_status=[DisputeStatus.none]
    )
    filtered_match_info = sdk_client.live_asset_service.query_live_match(filtered_match_retrieve_param)
    print("use query_live_match to retrieve match info with some filters")
    print(json.dumps(filtered_match_info))

    # Option4: use retrieve_all_live_match to collect match info page by page
    all_asset_match_info = sdk_client.live_asset_service.retrieve_all_live_match(filtered_asset_match_retrieve_param)
    print("use retrieve_all_live_match to retrieve collect all asset match info with some filters")
    print("retrieve all the asset match info with filters, count=", len(all_asset_match_info))
    print("sample data for the whole asset match info, data=", json.dumps(all_asset_match_info[:5]))

    all_match_info = sdk_client.live_asset_service.retrieve_all_live_match(filtered_match_retrieve_param)
    print("use retrieve_all_live_match to retrieve collect all match info with some filters")
    print("retrieve all the match info with filters, count=", len(all_match_info))
    print("sample data for the whole match info, data=", json.dumps(all_match_info[:5]))


if __name__ == "__main__":
    main()
