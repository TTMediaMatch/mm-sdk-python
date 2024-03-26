from .auth.authentication import Authentication
from .upload.video_upload import VideoUpload
from .upload.live_upload import LiveUpload


class MediaMatchSDKClient:
    def __init__(self, clientID=None, clientSecret=None):
        # Initialize the authentication component and log in to get the access token
        self.live_upload_service = None
        self.video_upload_service = None
        self.auth = Authentication(clientID, clientSecret)
        self.access_token = self.auth.login()

        # Initialize other components of the SDK
        self.refresh_services()

    def refresh_services(self):
        """Initialize or refresh the services with the current access token."""
        self.video_upload_service = VideoUpload(self.access_token)
        self.live_upload_service = LiveUpload(self.access_token)

    def refresh_token(self):
        self.access_token = self.auth.login()
        self.refresh_services()
