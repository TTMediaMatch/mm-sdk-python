# MM-SDK-Python

Welcome to the MediaMatch Python SDK! This SDK allows you to interact with MediaMatch conveniently within your Python applications.

## Installation

This SDK requires Python version 3.0 or higher.

To install the SDK, run the following command:

```sh
pip install git+https://github.com/TTMediaMatch/mm-sdk-python.git
```

## Getting Started

### Retrieve Access Token

To start using the SDK, you'll first need to retrieve an access token using your `ClientID` and `ClientSecret`. An example of this can be found at:

- [examples/example_authentication.py](https://github.com/TTMediaMatch/mm-sdk-python/blob/main/mediamatch_sdk/examples/example_authentication.py)

You have two options for authenticating your SDK client:

#### Option 1: Use `ClientID` and `ClientSecret` Directly in Code

```python
from mm_sdk_python import MediaMatchSDKClient

sdk_client = MediaMatchSDKClient('your_client_id', 'your_client_secret')
```

#### Option 2: Set Environment Variables
Alternatively, you can set your credentials in environment variables and initialize the MediaMatchSDKClient without any arguments.

``` arduino
export MM_CLIENT_ID="your_client_id"
export MM_CLIENT_SECRET="your_client_secret"
```

Then in your code:

```python
from mm_sdk_python import MediaMatchSDKClient

sdk_client = MediaMatchSDKClient()
```
## Features

### Video Upload

You can upload videos either from a local file or via a URL.

#### Upload from a Local File

For uploading videos from a local file, follow these steps:

1. Create a delivery batch job.
2. Upload the file by chunks.

See the example at [examples/example_upload_video_reference_by_local_upload.py](https://github.com/TTMediaMatch/mm-sdk-python/blob/main/mediamatch_sdk/examples/example_upload_video_reference_by_local_upload.py).

#### Upload by URL

To upload a video using its URL address, pass in the URL when creating the delivery job,
refer to the example at:

[examples/example_upload_video_reference_by_pull_from_url.py](https://github.com/TTMediaMatch/mm-sdk-python/blob/main/mediamatch_sdk/examples/example_upload_video_reference_by_pull_from_url.py)

### Live Upload

To create a new live upload session and retrieve the streaming address, see:

[examples/example_create_live_reference_delivery.py](https://github.com/TTMediaMatch/mm-sdk-python/blob/main/mediamatch_sdk/examples/example_create_live_reference_delivery.py)


## API Specification

For more detailed information about the API and its functionalities, please refer to the API specification documentation:

[API Specification Documentation](mediamatch help article url)