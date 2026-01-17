import requests

host = "ipc.gps555.net"
uid = "112296667870" #Your camera's Unique ID
bearer_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im1pcm9sZW50YWlAZ21haWwuY29tIiwiZXhwIjoxNzY5NDU5MzQ2LCJmYW1pbHlfaWQiOjAsImxhbmciOiJsdCIsIm9yaWdfaWF0IjoxNzY4MTYzMzQ2LCJyb2xlX2lkIjoyLCJ1c2VyX2lkIjo1ODM4MTYsInVzZXJuYW1lIjoibWlyb2xlbnRhaUBnbWFpbC5jb20ifQ.XP3mxBgueZnfheitujEgnH9ttaFvSRzrv4c6ItecQ5M"
def get_camera_info():
    # The API endpoint identified in the capture
    url = f"http://{host}/api/v1/ipc/%7Buid%7D"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent": "Dart/3.9 (dart:io)",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()

print(get_camera_info())
