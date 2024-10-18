import numpy as np
import matplotlib.pyplot as plt

# Given bit sequence and parameters
bit_sequence = [1, 0, 1, 1, 0]
bit_rate = 5
sampling_rate = 500  # Number of samples per second
carrier_frequency = 20  # Carrier frequency in Hz

# Time array for 1 second
time = np.linspace(0, 1, sampling_rate)

# Carrier signal
carrier_signal = np.sin(2 * np.pi * carrier_frequency * time)
modulated_signal = np.zeros_like(time)

# Calculate segment duration
segment_duration = 1 / bit_rate  # Each bit lasts for 1/5 seconds
segment_length = int(segment_duration * sampling_rate)  # Number of samples per segment

# Initialize NRZ-I signal
nrz_signal = np.zeros_like(time)
current_level = 1  # Initial signal level (1 for positive)

# Create NRZ-I encoded signal
for i, bit in enumerate(bit_sequence):
    # Calculate the time range for the current bit
    start_index = i * segment_length
    end_index = start_index + segment_length
    
    # Ensure the end_index does not exceed the length of time
    if end_index > len(time):
        end_index = len(time)
    
    if i == 0:
        # First bit does not invert if it is 1, just set the level
        if bit == 1:
            nrz_signal[start_index:end_index] = current_level
    else:
        if bit == 1:
            # If bit is 1 (and not the first bit), invert the current level
            current_level *= -1
            
        # Set the NRZ-I signal for the current bit duration
        nrz_signal[start_index:end_index] = current_level

# Modulate the signal based on the NRZ-I encoded signal
for i in range(len(bit_sequence)):
    start_index = i * segment_length
    end_index = start_index + segment_length
    if end_index > len(time):
        end_index = len(time)
    
    # Use the carrier signal if NRZ-I is 1, or 0 if NRZ-I is -1
    modulated_signal[start_index:end_index] = nrz_signal[start_index:end_index] * np.sin(2 * np.pi * carrier_frequency * time[start_index:end_index])

# Binary signal for visualization using NRZ-I
nrz_binary_signal = np.zeros_like(time)
current_level = 1  # Reset for NRZ-I binary representation

for i in range(len(bit_sequence)):
    start_index = i * segment_length
    end_index = start_index + segment_length
    
    # Set the NRZ-I binary signal for the current bit duration
    if i == 0 and bit_sequence[i] == 1:
        # First bit stays positive
        nrz_binary_signal[start_index:end_index] = current_level
    else:
        if bit_sequence[i] == 1:
            current_level *= -1
        nrz_binary_signal[start_index:end_index] = current_level

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Plot NRZ-I Binary Signal
ax.plot(time, nrz_binary_signal + 2.4, color='red', lw=2, label="NRZ-I Binary Signal")
ax.text(0.5, 1.1, 'NRZ-I Binary Signal', fontsize=12, color='black', verticalalignment='bottom')

# Plot Carrier Signal
ax.plot(time, carrier_signal, color='black', lw=2, label="Carrier Signal", alpha=0.7)

# Plot Modulated Signal
ax.plot(time, modulated_signal - 2.5, color='magenta', lw=2, label="Modulated Signal")
ax.text(0.5, -3.6, 'Modulated Signal', fontsize=12, color='magenta', verticalalignment='top')

# Annotate the bits
for i, bit in enumerate(bit_sequence):
    ax.text(i * segment_duration + 0.05, 3.5, str(bit), fontsize=12, color='black')

# Formatting the plot
ax.set_xlabel('Time (s)', fontsize=12)
ax.set_ylabel('Amplitude', fontsize=12)
ax.set_xticks(np.linspace(0, 1, len(bit_sequence) + 1))
ax.set_xticklabels([])
ax.set_yticks([])
ax.set_xlim([0, 1])
ax.set_ylim([-4, 4])
ax.grid(True)

# Legend
ax.legend(loc='lower left')

plt.tight_layout()
plt.show()
