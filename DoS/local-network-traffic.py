import socket
import random
import time
# Camera details
TARGET_IP = "192.168.137.240"
TARGET_PORT = 80 

def unsolicited_traffic_test(duration_seconds=10):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    bytes_to_send = random._urandom(1024) # 1KB of garbage data
    
    timeout = time.time() + duration_seconds
    sent_count = 0
    
    print(f"Sending unsolicited traffic to {TARGET_IP}...")
    while time.time() < timeout:
        client.sendto(bytes_to_send, (TARGET_IP, TARGET_PORT))
        sent_count += 1
    
    print(f"Test complete. Total packets sent: {sent_count}")

unsolicited_traffic_test(10)