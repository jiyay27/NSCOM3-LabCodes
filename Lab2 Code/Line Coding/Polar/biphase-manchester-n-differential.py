import matplotlib.pyplot as plt
import numpy as np

# Binary data to encode
data = [0,1,0,0,1,1]

# Parameters for the signal
bit_duration = 1  # duration of each bit
sampling_rate = 1000  # samples per second
samples_per_bit = sampling_rate // 2  # each half-bit is sampled at this rate

# Time axis for the entire signal
total_time = np.linspace(0, bit_duration * len(data), sampling_rate * len(data), endpoint=False)

# Manchester Encoding
manchester_signal = np.zeros(sampling_rate * len(data))

for i, bit in enumerate(data):
    if bit == 1:
        # '1' is low-to-high transition (first half low, second half high)
        manchester_signal[i * sampling_rate: i * sampling_rate + samples_per_bit] = -1
        manchester_signal[i * sampling_rate + samples_per_bit: (i + 1) * sampling_rate] = 1
    elif bit == 0:
        # '0' is high-to-low transition (first half high, second half low)
        manchester_signal[i * sampling_rate: i * sampling_rate + samples_per_bit] = 1
        manchester_signal[i * sampling_rate + samples_per_bit: (i + 1) * sampling_rate] = -1

# Differential Manchester Encoding
differential_manchester_signal = np.zeros(sampling_rate * len(data))

# Assume the initial level starts at -1
current_level = -1
for i, bit in enumerate(data):
    if bit == 1:
        # '1' causes a transition at the start of the bit
        current_level = -current_level  # Invert the level
        differential_manchester_signal[i * sampling_rate: i * sampling_rate + samples_per_bit] = current_level
        differential_manchester_signal[i * sampling_rate + samples_per_bit: (i + 1) * sampling_rate] = -current_level
    elif bit == 0:
        # '0' does not cause a transition at the start but there is still a middle transition
        differential_manchester_signal[i * sampling_rate: i * sampling_rate + samples_per_bit] = current_level
        differential_manchester_signal[i * sampling_rate + samples_per_bit: (i + 1) * sampling_rate] = -current_level

# Plotting both Manchester and Differential Manchester Encodings
plt.figure(figsize=(12, 8))

# Plot for Manchester Encoding
plt.subplot(2, 1, 1)
plt.plot(total_time, manchester_signal, drawstyle='steps-post', color='blue', linewidth=2)
plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Add horizontal line at y=0
plt.title('Manchester Encoding')
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xlim(0, len(data) * bit_duration)

# Add bit markers for Manchester
for i, bit in enumerate(data):
    plt.text(i * bit_duration + 0.5 * bit_duration, 1.2, f'{bit}', ha='center', color='black')

# Plot for Differential Manchester Encoding
plt.subplot(2, 1, 2)
plt.plot(total_time, differential_manchester_signal, drawstyle='steps-post', color='red', linewidth=2)
plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Add horizontal line at y=0
plt.title('Differential Manchester Encoding')
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.xlim(0, len(data) * bit_duration)

# Add bit markers for Differential Manchester
for i, bit in enumerate(data):
    plt.text(i * bit_duration + 0.5 * bit_duration, 1.2, f'{bit}', ha='center', color='black')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
