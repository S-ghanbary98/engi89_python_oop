# API Interactions
## pip is a package manager in python to intall packages that are not available.
# To install `requests package`
# `pip install requests`

import requests

requests_api = requests.get("https://www.bbc.co.uk/")

print(requests_api.status_code) # 200 for success - 404 and above
print(requests_api.headers)
print(type(requests_api.content))

