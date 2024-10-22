import numpy as np
import matplotlib.pyplot as plt

bit_sequence = [1, 0, 1, 1, 1, 0]
bit_duration = 1
sample_rate = 1000
t = np.linspace(0, bit_duration, int(sample_rate * bit_duration), endpoint=False)

f1 = 10
f2 = 5

signal = []
for bit in bit_sequence:
    if bit == 1:
        signal.extend(np.sin(2 * np.pi * f1 * t))
    else:
        signal.extend(np.sin(2 * np.pi * f2 * t))

time = np.linspace(0, bit_duration * len(bit_sequence), len(signal), endpoint=False)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.step(np.arange(len(bit_sequence) + 1) * bit_duration, 
         np.append(bit_sequence, bit_sequence[-1]), 
         where='post', color='red', linewidth=2)
plt.ylim(-0.5, 1.5)
plt.xlim(0, bit_duration * len(bit_sequence)) 
plt.ylabel('Bit Value')
plt.title('Binary Data')
plt.grid()

# Plot FSK signal
plt.subplot(2, 1, 2)
plt.plot(time, signal, color='blue')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('FSK Signal')
plt.xlim(0, bit_duration * len(bit_sequence)) 
plt.grid()

plt.tight_layout()
plt.show()



