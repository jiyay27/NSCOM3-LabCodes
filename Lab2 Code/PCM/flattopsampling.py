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

# Flat-Top Sampling (c): Flat horizontal bars holding sample value constant with vertical bars
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