# 2.1 Bandwidth of FSK

def calculate_fsk_bandwidth(d, S, delta_f):
    bandwidth = (1 + d) * S + 2 * delta_f
    return bandwidth

d = 1
S = 25000
delta_f = 25000

bandwidth = calculate_fsk_bandwidth(d, S, delta_f)
print(f"The required FSK bandwidth is {bandwidth / 1000} kHz")