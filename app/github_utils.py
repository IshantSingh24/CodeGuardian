import requests

def get_diff(diff_url: str):

    response = requests.get(diff_url)

    response.raise_for_status()

    return response.text