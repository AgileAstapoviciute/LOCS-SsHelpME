import requests

# Base configuration
BASE_URL = "http://ipc.gps555.net"
# Extracted from the authorization header in the pcap file
AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNpbHZpYS5ob3JnYUBjbm12LnJvIiwiZXhwIjoxNzY5NzMwNzc3LCJmYW1pbHlfaWQiOjAsImxhbmciOiJlbiIsIm9yaWdfaWF0IjoxNzY4NDM0Nzc3LCJyb2xlX2lkIjoyLCJ1c2VyX2lkIjo4MzQ4NTMsInVzZXJuYW1lIjoic2lsdmlhLmhvcmdhQGNubXYucm8ifQ.V6lYDCH_fJIybEhOdLAlXEoi-7mXvBXHxXr12X0fqt4"
headers = {
    "user-agent": "Dart/3.9 (dart:io)",
    "language": "en",
    "authorization": AUTH_TOKEN,
    "content-type": "application/json"
}

def query_api(endpoint, params=None):
    url = f"{BASE_URL}{endpoint}"
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        print(f"--- Endpoint: {endpoint} ---")
        print(response.json())
        print("\n")
    except requests.exceptions.RequestException as e:
        print(f"Error querying {endpoint}: {e}")

endpoints = [
    "/api/v1/ip/get-country",        # Get IP-based country info
    "/api/v1/lang/en",               # Language configuration (English)
    "/api/v1/ipc-function",          # IPC functionality info
    "/api/v1/ipc"                    # IPC status/terminal info
]

# Querying endpoints with specific parameters found in the capture
if __name__ == "__main__":
    # Query standard endpoints
    query_api("/api/v1/ip/get-country", params={"ipAddress": ""})
    query_api("/api/v1/lang/en")
    query_api("/api/v1/ipc-function")
    
    # Query IPC endpoint with terminalFamilyId found in the capture
    query_api("/api/v1/ipc", params={"terminalFamilyId": "834853"})