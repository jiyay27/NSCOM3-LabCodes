import matplotlib.pyplot as plt
import numpy as np

# Define signal parameters
T = 1  # period (seconds)
fs = 500  # sampling frequency (Hz) 
time = np.linspace(0, T, T * fs, endpoint=False)

# Generate sine wave
frequency_sine = 5  # frequency (Hz)
sine_wave = np.sin(2 * np.pi * frequency_sine * time)

# Generate square wave
frequency_square = 2  # frequency (Hz)
duty_cycle = 0.01  # percentage of the period where the signal is high
square_wave = np.where(
    np.mod(np.floor(2 * duty_cycle * fs * time), 2) == 0, 1, -1)

plt.axhline(y = 0, color = 'k')
plt.plot(time, square_wave)
plt.show()