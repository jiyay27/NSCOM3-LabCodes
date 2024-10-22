import numpy as np
import matplotlib.pyplot as plt

# Define parameters
bit_sequence = [0, 1, 0, 1]
bit_sequence_2 = [0, 0, 1, 1]
bit_rate = 5  # Bit rate in bits per second (Hz)
cycles_per_bit = 4  # Number of carrier wave cycles per bit
carrier_frequency = bit_rate * cycles_per_bit  # Carrier frequency in Hz

# Calculate the total number of samples and time vector
total_time = len(bit_sequence) / bit_rate  # Total time in seconds
samples_per_bit = 500 // len(bit_sequence)
time = np.linspace(0, total_time, samples_per_bit * len(bit_sequence))  # Full time vector

# Initialize signals
signal_1 = np.zeros(len(time))
modulated_signal_1 = np.zeros(len(time))

# Carrier signal for the entire duration (completes integer cycles per bit)
carrier_signal_1 = np.sin(2 * np.pi * carrier_frequency * time)

# Initialize signals
signal_2 = np.zeros(len(time))
modulated_signal_2 = np.zeros(len(time))

# Carrier signal for the entire duration (completes integer cycles per bit)
carrier_signal_2 = np.sin(2 * np.pi * carrier_frequency * time)

# Fill signal_1 and modulated_signal_1 based on bit_sequence
for i, bit in enumerate(bit_sequence):
    start_index = i * samples_per_bit
    end_index = (i + 1) * samples_per_bit

    # Apply the 90-degree phase shift to the entire sequence
    modulated_signal_1[start_index:end_index] = np.sin(2 * np.pi * carrier_frequency * time[start_index:end_index] + np.pi)

    # Further phase adjustment based on the bit value
    if bit == 1:
        # Apply an additional 180-degree phase shift for bit 1
        modulated_signal_1[start_index:end_index] = np.sin(2 * np.pi * carrier_frequency * time[start_index:end_index] + np.pi/2 + np.pi + 1.5)
    # No need to do anything special for bit 0, as it's already set with the 90-degree shift

    # Set the binary signal for this bit
    signal_1[start_index:end_index] = bit

# Fill signal_2 and modulated_signal_2 based on bit_sequence
for i, bit in enumerate(bit_sequence_2):
    start_index = i * samples_per_bit
    end_index = (i + 1) * samples_per_bit
    
    # Apply the 90-degree phase shift to the entire sequence
    modulated_signal_2[start_index:end_index] = np.sin(2 * np.pi * carrier_frequency * time[start_index:end_index] + np.pi)

    # Further phase adjustment based on the bit value
    if bit == 1:
        # Apply an additional 180-degree phase shift for bit 1
        modulated_signal_2[start_index:end_index] = np.sin(2 * np.pi * carrier_frequency * time[start_index:end_index] + np.pi/2 + np.pi + 1.5)
    # No need to do anything special for bit 0, as it's already set with the 90-degree shift

    # Set the binary signal for this bit
    signal_2[start_index:end_index] = bit



# Create the subplots grid: 6 rows and 1 column for 6 different graphs
fig, axes = plt.subplots(7, 1, figsize=(10, 12), sharex=True)

# Define bit boundaries for x-axis ticks
bit_boundaries = np.linspace(0, total_time, len(bit_sequence) + 1)

# Plot the binary signal in the first subplot
axes[0].plot(time, signal_1, color='red', lw=3, label="First Binary Signal")
axes[0].set_ylim([-1.5, 1.5])
axes[0].legend(loc='lower left')
axes[0].grid(True)

# Add vertical lines at bit boundaries for better alignment with grid
for boundary in bit_boundaries:
    axes[0].axvline(boundary, color='gray', linestyle='--')

# Plot the carrier signal in the middle (second subplot)
axes[1].plot(time, carrier_signal_1, color='black', lw=1.5, label="Carrier Signal", alpha=0.7)
axes[1].set_ylim([-1.5, 1.5])
axes[1].legend(loc='lower left')
axes[1].grid(True)

# Add vertical lines at bit boundaries
for boundary in bit_boundaries:
    axes[1].axvline(boundary, color='gray', linestyle='--')

# Plot the modulated signal in the third subplot
axes[2].plot(time, modulated_signal_1, color='cyan', lw=2, label="Modulated Signal")
axes[2].set_ylim([-1.5, 1.5])
axes[2].legend(loc='lower left')
axes[2].grid(True)

# Add vertical lines at bit boundaries
for boundary in bit_boundaries:
    axes[2].axvline(boundary, color='gray', linestyle='--')

#
axes[3].plot(time, signal_2, color='red', lw=3, label="Second Binary Signal")
axes[3].set_ylim([-1.5, 1.5])
axes[3].legend(loc='lower left')
axes[3].grid(True)
    
# Add vertical lines at bit boundaries
for boundary in bit_boundaries:
    axes[3].axvline(boundary, color='gray', linestyle='--')

axes[4].plot(time, carrier_signal_2, color='black', lw=1.5, label="Second Carrier Signal", alpha=0.7)
axes[4].set_ylim([-1.5, 1.5])
axes[4].legend(loc='lower left')
axes[4].grid(True)
    
# Add vertical lines at bit boundaries
for boundary in bit_boundaries:
    axes[4].axvline(boundary, color='gray', linestyle='--')

axes[5].plot(time, modulated_signal_2, color='cyan', lw=1.5, label="Second Modulated Signal")
axes[5].set_ylim([-1.5, 1.5])
axes[5].legend(loc='lower left')
axes[5].grid(True)
    
# Add vertical lines at bit boundaries
for boundary in bit_boundaries:
    axes[5].axvline(boundary, color='gray', linestyle='--')



sum_signal = modulated_signal_1 + modulated_signal_2

axes[6].plot(time, sum_signal, lw=1.5, label="Sum Signal")
axes[6].set_ylim([-1.5, 1.5])
axes[6].legend(loc='lower left')
axes[6].grid(True)
    
# Add vertical lines at bit boundaries
for boundary in bit_boundaries:
    axes[6].axvline(boundary, color='gray', linestyle='--')

# Set the x-ticks at bit boundaries to make sure the grid aligns with bits
axes[-1].set_xticks(bit_boundaries)

# Formatting the plot
axes[-1].set_xlabel('Time (s)')

plt.tight_layout()
plt.show()
