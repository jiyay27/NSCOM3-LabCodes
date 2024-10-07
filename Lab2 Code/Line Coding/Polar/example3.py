# Given values
bit_rate = 1_000_000  # 1 Mbps
c = 0.5  # average case
N = 1  # number of levels in NRZ-I

signal_rate = c * N * bit_rate

# Minimum bandwidth is equal to the signal rate in NRZ-I
min_bandwidth = signal_rate  # in Hz

print(f"Average Signal Rate (S): {signal_rate / 1000} kbaud")
print(f"Minimum Bandwidth (Bmin): {min_bandwidth / 1000} kHz")

