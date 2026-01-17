import requests

# API configuration based on the provided pcapng data
url = "http://ipc.gps555.net/api/v1/ipc/"
headers = {
    "Host": "ipc.gps555.net",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1pcm9sZW50YWlAZ21haWwuY29tIiwiZXhwIjoxNzY5NDU5MzQ2LCJmYW1pbHlfaWQiOjAsImxhbmciOiJsdCIsIm9yaWdfaWF0IjoxNzY4MTYzMzQ2LCJyb2xlX2lkIjoyLCJ1c2VyX2lkIjo1ODM4MTYsInVzZXJuYW1lIjoibWlyb2xlbnRhaUBnbWFpbC5jb20ifQ.XP3mxBgueZnfheitujEgnH9ttaFvSRzrv4c6ItecQ5M",
    "User-Agent": "Dart/3.9 (dart:io)",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/json"
}

# Optional parameter found in the capture
params = {
    "terminalFamilyId": "583816"
}

try:
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        print("Success!")
        print(response.json())
    else:
        print(f"Failed with status code: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")