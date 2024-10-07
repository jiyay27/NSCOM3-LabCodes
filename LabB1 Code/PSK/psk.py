import numpy as np
import matplotlib.pyplot as plt

# Parameters for the PSK modulation
f_carrier = 2e3  # Carrier frequency (Hz)
data_rate = 500   # Data rate (bps)
t = np.linspace(0, 1, 1000)  # Time vector

# Generate a random binary data sequence
data_bits = np.random.randint(0, 2, 10)

# Convert data bits to a sequence of 1s and -1s (BPSK)
data_signal = np.repeat(data_bits * 2 - 1, 100)

# Generate the carrier signal
carrier = np.sin(2 * np.pi * f_carrier * t[:len(data_signal)])

# BPSK modulated signal
bpsk_signal = data_signal * carrier

# Plot the binary data bits
plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 1)
plt.step(np.arange(len(data_bits)), data_bits, where='mid')
plt.title("Binary Data (0s and 1s)")
plt.ylim(-0.5, 1.5)
plt.grid(True)

# Plot the carrier signal
plt.subplot(3, 1, 2)
plt.plot(t[:len(data_signal)], carrier)
plt.title("Carrier Signal")
plt.grid(True)

# Plot the BPSK modulated signal
plt.subplot(3, 1, 3)
plt.plot(t[:len(bpsk_signal)], bpsk_signal)
plt.title("BPSK Modulated Signal")
plt.grid(True)

plt.tight_layout()
plt.show()
