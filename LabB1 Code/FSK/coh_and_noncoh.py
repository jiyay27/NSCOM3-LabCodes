# 2.2 Coherent and Non-coherent
def calculate_fsk_bandwidth(d, S, delta_f, coherent=True):
    if not coherent:
        delta_f *= 1.1

    bandwidth = (1 + d) * S + 2 * delta_f
    return bandwidth

d = 1
S = 25000
delta_f = 25000

# Coherent FSK
bandwidth_coherent = calculate_fsk_bandwidth(d, S, delta_f, coherent=True)
print(f"Coherent FSK Bandwidth: {bandwidth_coherent / 1000} kHz")

# Non-coherent FSK
bandwidth_non_coherent = calculate_fsk_bandwidth(d, S, delta_f, coherent=False)
print(f"Non-Coherent FSK Bandwidth: {bandwidth_non_coherent / 1000} kHz")