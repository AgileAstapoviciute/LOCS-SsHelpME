def read_ue(bits, start):
    """Read unsigned Exp-Golomb code"""
    zeros = 0
    while start < len(bits) and bits[start] == '0':
        zeros += 1
        start += 1
    start += 1  # skip the 1
    value = int(bits[start:start+zeros], 2) if zeros > 0 else 0
    return (2**zeros - 1 + value, start + zeros)

def get_sps_dimensions(filename):
    with open(filename, "rb") as f:
        data = f.read()

    # Find SPS NAL unit (nal_type = 7)
    i = 0
    while i < len(data) - 4:
        if data[i] == 0x00 and data[i+1] == 0x00 and ((data[i+2] == 0x00 and data[i+3] == 0x01) or data[i+2] == 0x01):
            nal_start = i + (4 if data[i+2] == 0x00 else 3)
            nal_type = data[nal_start] & 0x1F
            if nal_type == 7:  # SPS
                sps = data[nal_start+1:]
                break
        i += 1
    else:
        print("No SPS found!")
        return

    # Convert SPS to bit string
    bits = ''
    for b in sps:
        bits += f"{b:08b}"

    # Skip first 8 bits (profile_idc, constraint flags)
    bits = bits[8:]

    # Read seq_parameter_set_id
    _, index = read_ue(bits, 0)

    # Read log2_max_frame_num_minus4
    _, index = read_ue(bits, index)

    # Read pic_order_cnt_type
    pic_order_cnt_type, index = read_ue(bits, index)
    if pic_order_cnt_type == 0:
        _, index = read_ue(bits, index)
    elif pic_order_cnt_type == 1:
        index += 1 + 1 + 1 + 1  # skip some bits
        _, index = read_ue(bits, index)
        _, index = read_ue(bits, index)
    
    # Read max_num_ref_frames
    _, index = read_ue(bits, index)
    
    # Read gaps_in_frame_num_value_allowed
    index += 1

    # Read pic_width_in_mbs_minus1
    pic_width_in_mbs_minus1, index = read_ue(bits, index)

    # Read pic_height_in_map_units_minus1
    pic_height_in_map_units_minus1, index = read_ue(bits, index)

    width = (pic_width_in_mbs_minus1 + 1) * 16
    height = (pic_height_in_map_units_minus1 + 1) * 16

    print(f"Camera resolution: {width}x{height}")

# Use the function
get_sps_dimensions(r"C:\Users\20232291\OneDrive - TU Eindhoven\Documents\Y3Q2\video_clean.h264")
