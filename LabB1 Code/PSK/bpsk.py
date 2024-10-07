import numpy as np
import matplotlib.pyplot as plt

# Parameters
f_carrier = 5  # Carrier frequency in Hz (for easy visualization)
sampling_rate = 1000  # Number of samples per second
time = np.linspace(0, 1, sampling_rate)  # Time vector for 1 second

# Binary data: 1 0 1 1 0 1 0
data_bits = np.array([1, 0, 1, 1, 0, 1, 0])
samples_per_bit = sampling_rate // len(data_bits)  # Ensure integer division

# Create a binary data signal as a step function (square wave)
data_signal = np.repeat(data_bits, samples_per_bit)

# Adjust the length of data_signal to match the carrier length
data_signal = data_signal[:len(time)]  # Trim if necessary

# Generate the carrier signal
carrier_signal = np.sin(2 * np.pi * f_carrier * time)

# BPSK modulated signal: invert the carrier when the bit is 0
modulated_signal = carrier_signal * (2 * data_signal - 1)

# Plot the binary data, carrier, and modulated signal
plt.figure(figsize=(12, 8))

# Plot the binary data
plt.subplot(3, 1, 1)
plt.step(np.linspace(0, 1, len(data_signal)), data_signal, color='r', linewidth=2, where='mid')
plt.title('Binary Data')
plt.ylim(-0.5, 1.5)
plt.grid(True)

# Plot the carrier signal
plt.subplot(3, 1, 2)
plt.plot(time, carrier_signal, color='k')
plt.title('Carrier Signal')
plt.grid(True)

# Plot the modulated signal
plt.subplot(3, 1, 3)
plt.plot(time, modulated_signal, color='b')
plt.title('PSK Modulated Signal')
plt.grid(True)

plt.tight_layout()
plt.show()
