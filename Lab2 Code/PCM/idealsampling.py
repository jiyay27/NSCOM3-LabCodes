import numpy as np
import matplotlib.pyplot as plt

# Time axis
t = np.linspace(0, 2 * np.pi, 1000)
analog_signal = np.sin(t)

# Sampling points
sampling_rate = 20  # 20 samples over the period
sample_points = np.arange(0, len(t), len(t) // sampling_rate)
sampled_signal = analog_signal[sample_points]

# Create figure and subplots
plt.figure(figsize=(12, 4))

# Ideal Sampling (a): Impulse-like samples
plt.plot(t, analog_signal, 'k--', label='Analog signal')  # Original analog signal
plt.stem(t[sample_points], sampled_signal, linefmt='magenta', markerfmt='ro', basefmt=' ')  # Sampled points as impulses
plt.title('a. Ideal Sampling')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, t[-1])  # Set x-axis limit to the full range of t

plt.tight_layout()
plt.show()
