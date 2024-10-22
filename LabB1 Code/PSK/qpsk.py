import numpy as np
import matplotlib.pyplot as plt

# QPSK Modulation Parameters
carrier_freq = 2e3  # Carrier frequency in Hz
sampling_rate = 1e5  # Sampling rate in Hz
symbol_rate = 1e3  # Symbol rate in symbols/second
symbol_duration = 1 / symbol_rate  # Duration of each symbol

# Time array for one symbol duration
t = np.arange(0, symbol_duration, 1/sampling_rate)

# QPSK bit mapping: 00 -> 45°, 01 -> 135°, 10 -> 315°, 11 -> 225°
bit_map = {
    '00': np.pi / 4,    # 45 degrees
    '01': 3 * np.pi / 4,  # 135 degrees
    '11': 5 * np.pi / 4,  # 225 degrees
    '10': 7 * np.pi / 4   # 315 degrees
}

# Random bitstream (multiple of 2)
bitstream = '01001110'  # Example bitstream (change as needed)
# Split into pairs of bits
bit_pairs = [bitstream[i:i+2] for i in range(0, len(bitstream), 2)]

# Carrier signals (I and Q components)
I_carrier = np.cos(2 * np.pi * carrier_freq * t)
Q_carrier = np.sin(2 * np.pi * carrier_freq * t)

# Modulated QPSK signal
qpsk_signal = np.array([])

for pair in bit_pairs:
    phase = bit_map[pair]  # Get phase for the current bit pair
    # I and Q components for this symbol
    I_modulated = np.cos(2 * np.pi * carrier_freq * t + phase) * I_carrier
    Q_modulated = np.sin(2 * np.pi * carrier_freq * t + phase) * Q_carrier
    # Add modulated signals
    modulated_symbol = I_modulated + Q_modulated
    qpsk_signal = np.concatenate((qpsk_signal, modulated_symbol))

# Time array for the entire signal
t_signal = np.arange(0, len(qpsk_signal) / sampling_rate, 1/sampling_rate)

# Create subplots to show bitstream, carrier signals, and modulated signal
fig, axs = plt.subplots(4, 1, figsize=(10, 12))

# Plot the bit stream
bitstream_plot = np.repeat([int(bit) for bit in bitstream], int(len(t)))
axs[0].step(np.arange(len(bitstream_plot)) / sampling_rate, bitstream_plot)
axs[0].set_title('Bit Stream')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Bit Value')
axs[0].set_ylim([-0.5, 1.5])
axs[0].grid(True)

# Plot I carrier
axs[1].plot(np.tile(t, len(bit_pairs)), np.tile(I_carrier, len(bit_pairs)))
axs[1].set_title('In-Phase (I) Carrier Signal')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)

# Plot Q carrier
axs[2].plot(np.tile(t, len(bit_pairs)), np.tile(Q_carrier, len(bit_pairs)))
axs[2].set_title('Quadrature (Q) Carrier Signal')
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Amplitude')
axs[2].grid(True)

# Plot the QPSK modulated signal
axs[3].plot(t_signal, qpsk_signal)
axs[3].set_title('QPSK Modulated Signal')
axs[3].set_xlabel('Time (s)')
axs[3].set_ylabel('Amplitude')
axs[3].grid(True)

plt.tight_layout()
plt.show()
