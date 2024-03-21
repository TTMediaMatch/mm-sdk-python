import json


def extract_error_message(response):
    """
    Extracts error message from the response object.

    Args:
        response: The response object from a request.

    Returns:
        A string containing the error message or a default error message
        if the actual message cannot be extracted.
    """
    default_error_msg = "An error occurred, but no additional details are available."

    # Check if the response content is not empty
    if response.content:
        try:
            # Attempt to parse the JSON content
            error_details = json.loads(response.content)
            # Attempt to extract the 'msg' field from the JSON object
            return error_details.get('msg', default_error_msg)
        except json.JSONDecodeError:
            # If parsing fails, return the default error message
            return default_error_msg
    else:
        # If the content is empty, return a specific error message indicating this
        return "The server returned an empty response."
