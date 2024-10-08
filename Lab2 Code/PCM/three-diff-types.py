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
plt.figure(figsize=(12, 8))

# Ideal Sampling (a): Impulse-like samples
plt.subplot(3, 1, 1)
plt.plot(t, analog_signal, 'k--', label='Analog signal')  # Original analog signal
plt.stem(t[sample_points], sampled_signal, linefmt='magenta', markerfmt='ro', basefmt=' ')  # Sampled points as impulses
plt.title('a. Ideal Sampling')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, t[-1])  # Set x-axis limit to the full range of t

# Natural Sampling (b): Follow the waveform between sample points (stair-step) and show vertical bars
plt.subplot(3, 1, 2)
plt.plot(t, analog_signal, 'k--', label='Analog signal')  # Original analog signal
for i in range(len(sample_points) - 1):
    # For natural sampling, draw the sampled waveform between consecutive sample points
    plt.plot(t[sample_points[i]:sample_points[i + 1]], analog_signal[sample_points[i]:sample_points[i + 1]], color='magenta',linewidth=2)
    # Add vertical bars from the x-axis to the signal level
    plt.vlines(t[sample_points[i]], 0, sampled_signal[i], color='magenta', linewidth=2)

plt.title('b. Natural Sampling')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, t[-1])  # Set x-axis limit to the full range of t

# Flat-Top Sampling (c): Flat horizontal bars holding sample value constant with vertical bars
plt.subplot(3, 1, 3)
plt.plot(t, analog_signal, 'k--', label='Analog signal')  # Original analog signal
for i in range(len(sample_points) - 1):
    # Define the length of the horizontal lines (flat-top)
    horizontal_line_length = 0.2  # Adjust this value for the length of horizontal lines
    
    # Flat top, hold the sample constant between sample points
    plt.hlines(sampled_signal[i], 
               t[sample_points[i]], 
               t[sample_points[i]] + horizontal_line_length,  # Keep left side fixed
               colors='magenta', linewidth=2)
    
    # Add vertical bars from the x-axis to the flat-top value
    plt.vlines(t[sample_points[i]], 0, sampled_signal[i], color='magenta', linewidth=2)
    
    # Add another vertical line to connect to the right end of the horizontal line
    plt.vlines(t[sample_points[i]] + horizontal_line_length, 0, sampled_signal[i], color='magenta', linewidth=2)

plt.title('c. Flat-Top Sampling')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.grid(True)
plt.xlim(0, t[-1])  # Set x-axis limit to the full range of t

plt.tight_layout()
plt.show()
