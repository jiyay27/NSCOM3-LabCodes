import math

def nyquist_bit_rate(bandwidth, levels):
    bit_rate = 2 * bandwidth * math.log2(levels)
    return bit_rate

bandwidth = 3000 
levels = 2  
bit_rate = nyquist_bit_rate(bandwidth, levels)
print(f"Maximum Bit Rate: {bit_rate:.2f} bps")

