from .auth.authentication import Authentication
from .upload.video_upload import VideoUpload


class MediaMatchSDKClient:
    def __init__(self, clientID=None, clientSecret=None):
        # Initialize the authentication component and log in to get the access token
        self.auth = Authentication(clientID, clientSecret)
        self.access_token = self.auth.login()

        # Initialize other components of the SDK with the access token
        self.video_upload_service = VideoUpload(self.access_token)

    # Example method to expose video upload functionality through the client
    # def upload_video(self, video_path, metadata):
    #     return self.video_upload.upload_video(video_path, metadata)

    # Example method to list all assets
    # def list_assets(self):
    #     return self.asset_management.list_assets()

    # Additional methods