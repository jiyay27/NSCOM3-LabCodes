import numpy as np
import matplotlib.pyplot as plt

# Define parameters
bit_sequence = [1, 0, 1, 1, 1, 0]
bit_duration = 1  
sample_rate = 1000  

t = np.linspace(0, bit_duration, int(sample_rate * bit_duration), endpoint=False)

# Assign frequencies
f1 = 18  
f2 = 5   #
carrier_frequency = 8  # Carrier frequency

# Generate the FSK signal
signal = []
for bit in bit_sequence:
    if bit == 1:
        signal.extend(np.sin(2 * np.pi * f1 * t))  # FSK for bit 1
    else:
        signal.extend(np.sin(2 * np.pi * f2 * t))  # FSK for bit 0

# Create a time vector for the entire FSK signal
total_time = np.linspace(0, bit_duration * len(bit_sequence), len(signal), endpoint=False)

# Generate the carrier signal
carrier = np.sin(2 * np.pi * carrier_frequency * total_time)

plt.figure(figsize=(12, 8))

# Plot binary data
plt.subplot(3, 1, 1)
plt.step(np.arange(len(bit_sequence) + 1) * bit_duration, 
         np.append(bit_sequence, bit_sequence[-1]), 
         where='post', color='red', linewidth=2)
plt.ylim(-0.5, 1.5)
plt.xlim(0, bit_duration * len(bit_sequence)) 
plt.ylabel('Bit Value')
plt.title('Binary Data')
plt.grid()

# Plot Carrier Signal
plt.subplot(3, 1, 2)
plt.plot(total_time, carrier, color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Carrier Signal')
plt.xlim(0, bit_duration * len(bit_sequence)) 
plt.grid()

# Plot Modulated Carrier Signal
plt.subplot(3, 1, 3)
plt.plot(total_time, signal, color='green')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Modulated Carrier Signal')
plt.xlim(0, bit_duration * len(bit_sequence)) 
plt.grid()

plt.tight_layout()
plt.show()
