from scapy.all import rdpcap, UDP, IP

# === CONFIG ===
pcap_file = r"C:\Users\20232291\OneDrive - TU Eindhoven\Documents\Y3Q2\just watching the stream with udp.pcap"
output_file = r"C:\Users\20232291\OneDrive - TU Eindhoven\Documents\Y3Q2\video_raw.h264"
camera_ip = "192.168.137.103"  # change to your camera IP
camera_port = 59544            # change to your camera UDP port

# === Read PCAP ===
packets = rdpcap(pcap_file)
payloads = []

for pkt in packets:
    if UDP in pkt and IP in pkt:
        ip_layer = pkt[IP]
        udp_layer = pkt[UDP]
        
        if ip_layer.src == camera_ip and udp_layer.dport == camera_port:
            raw_payload = bytes(udp_layer.payload)
            if raw_payload:
                payloads.append(raw_payload)

# === Reassemble payloads in order of capture ===
# If the camera uses sequence numbers inside the payload, you could parse them here.
# For now, we concatenate in capture order.

with open(output_file, "wb") as f:
    for p in payloads:
        f.write(p)

print(f"Done! Raw video saved to {output_file}")
