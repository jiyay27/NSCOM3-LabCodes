import math

def nyquist_bit_rate(bandwidth, levels):
    bit_rate = 2 * bandwidth * math.log2(levels)
    return bit_rate

def shannon_capacity(bandwidth, snr):
    capacity = bandwidth * math.log2(1 + snr)
    return capacity

def convert_bps_to_mbps(given):
    x = 0
    while x != 6:
        given /= 10
        x += 1
    return given

bandwidth = 1000000 # 1MHz to HZ
snr = 63 # Signal-to-Noise Ratio
levels = 4  # Levels of channel

capacity = convert_bps_to_mbps(shannon_capacity(bandwidth, snr))
print(f"Shannon Capacity: {capacity:.2f} Mbps")

bit_rate = convert_bps_to_mbps(nyquist_bit_rate(bandwidth, levels))
print(f"Maximum Bit Rate: {bit_rate:.2f} Mbps")



