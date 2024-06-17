from mediamatch_sdk.asset.live_asset_activate import LiveAssetActivate
from mediamatch_sdk.asset.live_asset_deactivate import LiveAssetDeactivate
from mediamatch_sdk.asset.live_asset_other_info_query import LiveAssetOtherInfoQuery
from mediamatch_sdk.asset.live_metadata_query import LiveMetadataQuery
from mediamatch_sdk.asset.live_metadata_update import LiveMetadataUpdate
from mediamatch_sdk.asset.video_asset_activate import VideoAssetActivate
from mediamatch_sdk.asset.video_asset_deactivate import VideoAssetDeactivate
from mediamatch_sdk.asset.video_asset_other_info_query import VideoAssetOtherInfoQuery
from mediamatch_sdk.asset.video_metadata_query import VideoMetadataQuery
from mediamatch_sdk.asset.video_metadata_update import VideoMetadataUpdate
from mediamatch_sdk.auth.authentication import Authentication
from mediamatch_sdk.upload.video_upload import VideoUpload
from mediamatch_sdk.upload.live_upload import LiveUpload
from mediamatch_sdk.asset.live_match_query import LiveMatchQuery
from mediamatch_sdk.asset.video_match_query import VideoMatchQuery


class MediaMatchSDKClient:
    def __init__(self, clientID=None, clientSecret=None):
        # Initialize the authentication component and log in to get the access token
        self.live_upload_service = None
        self.video_upload_service = None
        self.live_match_query_service = None
        self.video_match_query_service = None
        self.auth = Authentication(clientID, clientSecret)
        self.access_token = self.auth.login()
        self.video_asset_activate_service = None
        self.video_asset_deactivate_service = None
        self.live_asset_activate_service = None
        self.live_asset_deactivate_service = None
        self.video_metadata_query_service = None
        self.live_metadata_query_service = None
        self.video_asset_other_info_query_service = None
        self.live_asset_other_info_query_service = None
        self.video_metadata_update_service = None
        self.live_metadata_update_service = None

        # Initialize other components of the SDK
        self.refresh_services()

    def refresh_services(self):
        """Initialize or refresh the services with the current access token."""
        self.video_upload_service = VideoUpload(self.access_token)
        self.live_upload_service = LiveUpload(self.access_token)
        self.video_asset_activate_service = VideoAssetActivate(self.access_token)
        self.live_asset_activate_service = LiveAssetActivate(self.access_token)
        self.video_asset_deactivate_service = VideoAssetDeactivate(self.access_token)
        self.live_asset_deactivate_service = LiveAssetDeactivate(self.access_token)
        self.video_match_query_service = VideoMatchQuery(self.access_token)
        self.live_match_query_service = LiveMatchQuery(self.access_token)
        self.video_metadata_query_service = VideoMetadataQuery(self.access_token)
        self.live_metadata_query_service = LiveMetadataQuery(self.access_token)
        self.video_asset_other_info_query_service = VideoAssetOtherInfoQuery(self.access_token)
        self.live_asset_other_info_query_service = LiveAssetOtherInfoQuery(self.access_token)
        self.video_metadata_update_service = VideoMetadataUpdate(self.access_token)
        self.live_metadata_update_service = LiveMetadataUpdate(self.access_token)

    def refresh_token(self):
        self.access_token = self.auth.login()
        self.refresh_services()
