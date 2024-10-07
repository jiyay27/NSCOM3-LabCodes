import matplotlib.pyplot as plt
import numpy as np

data = [1, 0, 1, 1, 0, 0, 1, 0] # Binary data to encode

# Parameters for the signal
bit_duration = 1  # duration of each bit
sampling_rate = 1000  # samples per second
time_per_bit = np.linspace(0, bit_duration, sampling_rate, endpoint=False)
total_time = np.linspace(0, bit_duration * len(data), sampling_rate * len(data), endpoint=False)

# Polar NRZ encoding: 1 -> +1, 0 -> -1
polar_nrz_signal = np.array([1 if bit == 1 else -1 for bit in data])
signal = np.repeat(polar_nrz_signal, sampling_rate)

# Plot the signal
plt.figure(figsize=(10, 4))
plt.plot(total_time, signal, drawstyle='steps-post', color='green', linewidth=2)
plt.title('Polar NRZ Line Coding Scheme')
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.grid(True)

# Adding bit markers (above +1 and below -1 for 1s and 0s)
for i, bit in enumerate(data):
    if bit == 1:
        plt.text(i * bit_duration + 0.5 * bit_duration, 1.2, f'{bit}', ha='center', color='green')
    else:
        plt.text(i * bit_duration + 0.5 * bit_duration, -1.5, f'{bit}', ha='center', color='red')


plt.ylim(-1.5, 1.5)
plt.xlim(0, len(data) * bit_duration)
plt.show()


