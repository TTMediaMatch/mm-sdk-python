import json


def extract_log_id(response):
    if response.headers:
        return response.headers.get('X-Tt-Logid', '')
    return ''


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
            error_msg = error_details.get('msg', default_error_msg)
        except json.JSONDecodeError:
            # If parsing fails, return the default error message
            error_msg = default_error_msg
    else:
        # If the content is empty, return a specific error message indicating this
        error_msg = "The server returned an empty response."

    # Append log_id to the error message if it is not empty
    log_id = extract_log_id(response)
    if log_id:
        error_msg += f" \n(log_id: {log_id})"
    return error_msg
