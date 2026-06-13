import requests


def get_diff(pr_api_url: str):

    headers = {
        "Accept": "application/vnd.github.v3.diff",
        "User-Agent": "CodeGuardian"
    }

    response = requests.get(
        pr_api_url,
        headers=headers
    )

    print("\n====== DIFF REQUEST ======")
    print("URL:", pr_api_url)
    print("STATUS:", response.status_code)

    if response.status_code != 200:
        print(response.text[:1000])

        raise Exception(
            f"Failed to fetch diff. Status: {response.status_code}"
        )

    return response.text