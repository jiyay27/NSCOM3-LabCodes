import numpy as np
import matplotlib.pyplot as plt

# Time axis
t = np.linspace(0, 4 * np.pi, 1000)

# First wave: Digital signal
first_wave = np.piecewise(t, [t < np.pi, (t >= np.pi) & (t < 2 * np.pi), 
                              (t >= 2 * np.pi) & (t < 3 * np.pi), t >= 3 * np.pi], 
                          [-1, 1, -1, 1])

# Second and Fifth waves: Multiple sine waves
high_freq_wave = np.sin(1 * t)  # Higher frequency sine wave for continuous oscillation

# Third, Sixth, and Seventh waves: Amplitude modulated signal
modulation = 0.5 * np.sin(2 * t)  # Modulating signal
am_modulated_wave = (1 + modulation) * np.sin(5 * t)  # Amplitude-modulated signal

# Fourth wave: Easier digital signal
fourth_wave = np.piecewise(t, [t < 2 * np.pi, t >= 2 * np.pi], [-1, 1])

# Create figure and subplots
fig, axs = plt.subplots(7, 1, figsize=(10, 10), sharex=True)

# Define cycle boundaries for vertical lines
cycle_boundaries = np.arange(0, 4 * np.pi + np.pi, np.pi)

# Plot each wave on a separate subplot with cycle boundaries and horizontal line
for ax in axs:
    # Set horizontal line at y=0
    ax.axhline(y=0, color='black', linewidth=0.8, linestyle='--')

# Plot each wave
axs[0].plot(t, first_wave, 'r', linewidth=2)
axs[0].set_title('First Wave: Digital Signal (Correct)')
for boundary in cycle_boundaries:
    axs[0].axvline(x=boundary, color='gray', linestyle='--', linewidth=0.5)

axs[1].plot(t, high_freq_wave, 'b', linewidth=2)
axs[1].set_title('Second Wave: Continuous High-Frequency Sine Wave (Top Signal)')
for boundary in cycle_boundaries:
    axs[1].axvline(x=boundary, color='gray', linestyle='--', linewidth=0.5)

axs[2].plot(t, am_modulated_wave, 'g', linewidth=2)
axs[2].set_title('Third Wave: Amplitude Modulated Signal (Bottom Signal)')
for boundary in cycle_boundaries:
    axs[2].axvline(x=boundary, color='gray', linestyle='--', linewidth=0.5)

axs[3].plot(t, fourth_wave, 'r', linewidth=2)
axs[3].set_title('Fourth Wave: Easier Digital Signal (Correct)')
for boundary in cycle_boundaries:
    axs[3].axvline(x=boundary, color='gray', linestyle='--', linewidth=0.5)

axs[4].plot(t, high_freq_wave, 'b', linewidth=2)
axs[4].set_title('Fifth Wave: Continuous High-Frequency Sine Wave (Top Signal)')
for boundary in cycle_boundaries:
    axs[4].axvline(x=boundary, color='gray', linestyle='--', linewidth=0.5)

axs[5].plot(t, am_modulated_wave, 'g', linewidth=2)
axs[5].set_title('Sixth Wave: Amplitude Modulated Signal (Bottom Signal)')
for boundary in cycle_boundaries:
    axs[5].axvline(x=boundary, color='gray', linestyle='--', linewidth=0.5)

axs[6].plot(t, am_modulated_wave, 'g', linewidth=2)
axs[6].set_title('Seventh Wave: Amplitude Modulated Signal (Bottom Signal)')
for boundary in cycle_boundaries:
    axs[6].axvline(x=boundary, color='gray', linestyle='--', linewidth=0.5)

# Set x-axis labels and layout adjustments
for ax in axs:
    ax.set_yticks([])  # Hide y-axis ticks
    ax.grid(True)

plt.xlabel('Time')
plt.tight_layout()
plt.show()
