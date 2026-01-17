from scapy.all import rdpcap, UDP, IP

# === CONFIG ===
pcap_file = r"C:\Users\20232291\OneDrive - TU Eindhoven\Documents\Y3Q2\just watching the stream with udp.pcap"
output_file = r"C:\Users\20232291\OneDrive - TU Eindhoven\Documents\Y3Q2\video_clean.h264"
camera_ip = "192.168.1.100"  # replace with your camera IP
camera_port = 5000            # replace with your camera UDP port

# === Read PCAP ===
packets = rdpcap(pcap_file)
raw_video = bytearray()

for pkt in packets:
    if UDP in pkt and IP in pkt:
        ip_layer = pkt[IP]
        udp_layer = pkt[UDP]

        if ip_layer.src == camera_ip and udp_layer.dport == camera_port:
            payload = bytes(udp_layer.payload)
            
            # Look for H.264 start codes
            start = payload.find(b'\x00\x00\x00\x01')
            if start == -1:
                start = payload.find(b'\x00\x00\x01')
            if start != -1:
                raw_video += payload[start:]  # append only valid H.264 frame

# === Write cleaned video ===
with open(output_file, "wb") as f:
    f.write(raw_video)

print(f"Done! Clean H.264 saved to {output_file}")
