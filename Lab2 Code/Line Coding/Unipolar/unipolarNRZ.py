import matplotlib.pyplot as plt
import numpy as np

data = [1, 0, 1, 1, 0, 0, 1, 0] # Binary data to encode

# Parameters for the signal
bit_duration = 1  # duration of each bit
sampling_rate = 1000  # samples per second
time_per_bit = np.linspace(0, bit_duration, sampling_rate, endpoint=False)
total_time = np.linspace(0, bit_duration * len(data), sampling_rate * len(data), endpoint=False)

# Generate unipolar NRZ signal
signal = np.repeat(data, sampling_rate)

# Plot the signal
plt.figure(figsize=(10, 4))
plt.plot(total_time, signal, drawstyle='steps-post', color='blue', linewidth=2)
plt.title('Unipolar NRZ Line Coding Scheme')
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.grid(True)

# Adding bit markers
for i, bit in enumerate(data):
    plt.text(i * bit_duration + 0.5 * bit_duration, 1.2, f'{bit}', ha='center')

plt.ylim(0, 1.5)
plt.xlim(0, len(data) * bit_duration)
plt.show()


