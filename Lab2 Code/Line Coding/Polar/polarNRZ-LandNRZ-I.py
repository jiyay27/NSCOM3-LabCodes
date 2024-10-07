import matplotlib.pyplot as plt
import numpy as np

# Binary data to encode
data = [1, 0, 1, 1, 0, 0, 1, 0]

# Parameters for the signal
bit_duration = 1  # duration of each bit
sampling_rate = 1000  # samples per second
time_per_bit = np.linspace(0, bit_duration, sampling_rate, endpoint=False)
total_time = np.linspace(0, bit_duration * len(data), sampling_rate * len(data), endpoint=False)

# NRZ-L encoding: 1 -> +1, 0 -> -1
polar_nrz_signal = np.array([1 if bit == 1 else -1 for bit in data])
nrz_l_signal = np.repeat(polar_nrz_signal, sampling_rate)

# NRZ-I encoding
nrz_i_signal = np.zeros_like(data)
nrz_i_signal[0] = 1 if data[0] == 1 else 0  # Start with 1 if first bit is 1, otherwise 0

# NRZ-I inverts on every '1'
for i in range(1, len(data)):
    if data[i] == 1:
        nrz_i_signal[i] = -nrz_i_signal[i - 1]  # Invert signal for '1'
    else:
        nrz_i_signal[i] = nrz_i_signal[i - 1]   # Maintain the same level for '0'

nrz_i_full_signal = np.repeat(nrz_i_signal, sampling_rate)

# Plot both NRZ-L and NRZ-I
plt.figure(figsize=(12, 8))

# Plot for NRZ-L
plt.subplot(2, 1, 1)
plt.plot(total_time, nrz_l_signal, drawstyle='steps-post', color='green', linewidth=2)
plt.axhline(0, color='black', linestyle='-', linewidth=1)
plt.title('NRZ-L Line Coding Scheme')
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.grid(True)

# Position markers for NRZ-L
for i, bit in enumerate(data):
    plt.text(i * bit_duration + 0.5 * bit_duration, 1.1, f'{bit}', ha='center', color='black')  # Align both at 1.1

plt.ylim(-1.5, 1.5)
plt.xlim(0, len(data) * bit_duration)

# Plot for NRZ-I (No markers for bits)
plt.subplot(2, 1, 2)
plt.plot(total_time, nrz_i_full_signal, drawstyle='steps-post', color='blue', linewidth=2)
plt.axhline(0, color='black', linestyle='-', linewidth=1)
plt.title('NRZ-I Line Coding Scheme')
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xlim(0, len(data) * bit_duration)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()


