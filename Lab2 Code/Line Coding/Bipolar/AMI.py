import matplotlib.pyplot as plt
import numpy as np

# Time for 6 bits, 800 samples total
time = np.linspace(0, 6, 600)

# Bit sequences for AMI and Pseudoternary
ami_bits = [0, 1, 0, 0, 1, 0]
pseudo_bits_corrected = [0, 1, 0, 0, 1, 0]

# AMI Signal: Alternate polarity for '1's, '0' stays at zero
ami_signal = np.zeros_like(time)
last_pulse = -1  # Start the first pulse direction as negative

for i, bit in enumerate(ami_bits):
    if bit == 1:
        last_pulse *= -1  # Flip polarity
        ami_signal[i * 100:(i + 1) * 100] = last_pulse  # Set pulse for this bit

# Pseudoternary Signal: '0' alternates, '1' stays at zero
pseudo_signal = np.zeros_like(time)
last_pulse = -1  # Start the first pulse direction as negative

for i, bit in enumerate(pseudo_bits_corrected):
    if bit == 0:
        last_pulse *= -1  # Flip polarity
        pseudo_signal[i * 100:(i + 1) * 100] = last_pulse  # Set pulse for this bit

# Create figure and plot
plt.figure(figsize=(10, 6))

# Plot AMI Encoding
plt.subplot(2, 1, 1)
plt.plot(time, ami_signal, color='blue', linewidth=2)
plt.title('AMI Encoding')
plt.ylim([-1.5, 1.5])
plt.xlim([0, 6])  # Adjust x-axis to match time range
plt.ylabel('Amplitude')
plt.grid(True)

# Add bit markers for AMI
for i, bit in enumerate(ami_bits):
    plt.text(i + 0.5, 1.2, str(bit), fontsize=12, ha='center', color='black')

# Plot Pseudoternary Encoding
plt.subplot(2, 1, 2)
plt.plot(time, pseudo_signal, color='red', linewidth=2)
plt.title('Pseudoternary Encoding')
plt.ylim([-1.5, 1.5])
plt.xlim([0, 6])  # Adjust x-axis to match time range
plt.ylabel('Amplitude')
plt.grid(True)

# Set x-axis label
plt.xlabel('Time')

# Adjust layout and show plot
plt.tight_layout()
plt.show()