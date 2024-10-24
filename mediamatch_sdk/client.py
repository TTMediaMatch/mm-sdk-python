from mediamatch_sdk.asset.live_asset import LiveAsset
from mediamatch_sdk.asset.video_asset import VideoAsset
from mediamatch_sdk.auth.authentication import Authentication
from mediamatch_sdk.upload.video_upload import VideoUpload
from mediamatch_sdk.upload.live_upload import LiveUpload
from mediamatch_sdk.policy.usage_policy import UsagePolicy


class MediaMatchSDKClient:
    def __init__(self, clientID=None, clientSecret=None):
        # Initialize the authentication component and log in to get the access token
        self.live_upload_service = None
        self.video_upload_service = None
        self.live_asset_service = None
        self.video_asset_service = None
        self.usage_policy_service = None
        self.auth = Authentication(clientID, clientSecret)
        self.access_token = self.auth.login()

        # Initialize other components of the SDK
        self.refresh_services()

    def refresh_services(self):
        """Initialize or refresh the services with the current access token."""
        self.video_upload_service = VideoUpload(self.access_token)
        self.live_upload_service = LiveUpload(self.access_token)
        self.video_asset_service = VideoAsset(self.access_token)
        self.live_asset_service = LiveAsset(self.access_token)
        self.usage_policy_service = UsagePolicy(self.access_token)

    def refresh_token(self):
        self.access_token = self.auth.login()
        self.refresh_services()
