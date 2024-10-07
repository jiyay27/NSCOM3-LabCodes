import matplotlib.pyplot as plt
import numpy as np

# Binary data to encode
data = [1, 0, 1, 1, 0, 0, 1, 0]

# Parameters for the signal
bit_duration = 1  # duration of each bit (1 second)
sampling_rate = 1000  # samples per second
samples_per_bit = sampling_rate // 2  # RZ has two levels per bit (half high/low, half zero)

# Time axis for the entire signal
total_time = np.linspace(0, bit_duration * len(data), sampling_rate * len(data), endpoint=False)

# Initialize an array to store the Polar RZ signal
polar_rz_signal = np.zeros(sampling_rate * len(data))

# Loop over each bit in the data and assign Polar RZ values
for i, bit in enumerate(data):
    if bit == 1:
        # For '1', the signal goes to +1 for the first half and then returns to zero
        polar_rz_signal[i * sampling_rate: i * sampling_rate + samples_per_bit] = 1
    elif bit == 0:
        # For '0', the signal goes to -1 for the first half and then returns to zero
        polar_rz_signal[i * sampling_rate: i * sampling_rate + samples_per_bit] = -1

# Plot the Polar RZ signal
plt.figure(figsize=(12, 4))
plt.plot(total_time, polar_rz_signal, drawstyle='steps-post', linewidth=2, color='purple')
plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Add a horizontal line at y=0
plt.title('Polar RZ Line Coding Scheme')
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.grid(True)

# Add bit markers at the top of the plot
for i, bit in enumerate(data):
    plt.text(i * bit_duration + 0.5 * bit_duration, 1.2, f'{bit}', ha='center', color='black')

# Set the y-limits and x-limits to match the signal
plt.ylim(-1.5, 1.5)
plt.xlim(0, len(data) * bit_duration)

# Show the plot
plt.tight_layout()
plt.show()


