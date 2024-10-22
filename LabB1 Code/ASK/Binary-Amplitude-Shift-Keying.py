import numpy as np
import matplotlib.pyplot as plt

# Define parameters
bit_sequence = [1, 0, 1, 1, 0]
bit_rate = 5  # Base bit rate for time scaling
baud_rate = 5
time = np.linspace(0, 1, 500)
signal = np.zeros_like(time)

# Create the signal based on bit sequence, with flat line for '0' and higher frequency for '1'
for i, bit in enumerate(bit_sequence):
    if bit == 1:
        signal[i*100:(i+1)*100] = np.sin(2 * np.pi * 15 * time[i*100:(i+1)*100])  # Higher frequency for bit '1'
    else:
        signal[i*100:(i+1)*100] = 0  # Flat signal for bit '0'

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the signal waveform
ax.plot(time, signal, color='b', lw=2)

# Add title and labels
ax.set_title(f'Bit rate: {bit_rate}, Baud rate: {baud_rate}', fontsize=14)
ax.set_xlabel('Time (s)', fontsize=12)
ax.set_ylabel('Amplitude', fontsize=12)
ax.set_xticks(np.linspace(0, 1, len(bit_sequence)+1))
ax.set_xticklabels(['']*6)
ax.set_yticks([-1, 0, 1])
ax.set_xlim([0, 1])
ax.set_ylim([-1.5, 1.5])
ax.grid(True)

# Add bit sequence labels and signal element annotations
for i, bit in enumerate(bit_sequence):
    ax.text(i/5 + 0.08, 1.3, str(bit), fontsize=12, color='magenta')
    ax.text(i/5 + 0.05, -1.3, '1 signal\n element', fontsize=10)

# Add time, bit rate, and baud rate annotations
ax.annotate('', xy=(0, -1.5), xytext=(1, -1.5), arrowprops=dict(arrowstyle='<->'))
ax.text(0.45, -1.8, '1 s', fontsize=12)
ax.annotate('', xy=(1.02, 0), xytext=(1.02, -1.5), arrowprops=dict(arrowstyle='<->'))
ax.text(1.05, -0.75, 'Time', fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
