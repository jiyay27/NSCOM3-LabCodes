import numpy as np
import matplotlib.pyplot as plt

# Define the original sine wave
f = 1  # Frequency of the sine wave
t = np.linspace(0, 1, 1000)  # Time vector
original_signal = np.sin(2 * np.pi * f * t)

# Sampling rates
fs_2nyquist = 4 * f
fs_nyquist = 2 * f
fs_halfnyquist = f

# Sampling points
t_2nyquist = np.arange(0, 1, 1/fs_2nyquist)
t_nyquist = np.arange(0, 1, 1/fs_nyquist)
t_halfnyquist = np.arange(0, 1, 1/fs_halfnyquist)

# Sampled signals
sampled_2nyquist = np.sin(2 * np.pi * f * t_2nyquist)
sampled_nyquist = np.sin(2 * np.pi * f * t_nyquist)
sampled_halfnyquist = np.sin(2 * np.pi * f * t_halfnyquist)

# Plotting
fig, axs = plt.subplots(3, 2, figsize=(12, 8))

# Nyquist rate sampling (fs = 2f)
axs[0, 0].plot(t, original_signal, 'r', label='Original Signal')
axs[0, 0].plot(t_nyquist, sampled_nyquist, 'ko', label='Sampled Points')
axs[0, 0].set_title('a. Nyquist rate sampling: fs = 2f')
axs[0, 1].stem(t_nyquist, sampled_nyquist, 'ko', basefmt=" ", label='Reconstructed Signal')
axs[0, 1].set_title('Reconstructed Signal')

# Oversampling (fs = 4f)
axs[1, 0].plot(t, original_signal, 'r', label='Original Signal')
axs[1, 0].plot(t_2nyquist, sampled_2nyquist, 'ko', label='Sampled Points')
axs[1, 0].set_title('b. Oversampling: fs = 4f')
axs[1, 1].stem(t_2nyquist, sampled_2nyquist, 'ko', basefmt=" ", label='Reconstructed Signal')
axs[1, 1].set_title('Reconstructed Signal')

# Undersampling (fs = f)
axs[2, 0].plot(t, original_signal, 'r', label='Original Signal')
axs[2, 0].plot(t_halfnyquist, sampled_halfnyquist, 'ko', label='Sampled Points')
axs[2, 0].set_title('c. Undersampling: fs = f')
axs[2, 1].stem(t_halfnyquist, sampled_halfnyquist, 'ko', basefmt=" ", label='Reconstructed Signal')
axs[2, 1].set_title('Reconstructed Signal')

for ax in axs.flat:
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()