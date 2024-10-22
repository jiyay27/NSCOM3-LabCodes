import numpy as np
import matplotlib.pyplot as plt

bit_sequence = [0, 1, 0, 1]
bit_sequence_2 = [0, 0, 1, 1]
bit_sequence_3 = [1,2,3,4]
bit_rate = 5  
cycles_per_bit = 3  
carrier_frequency = bit_rate * cycles_per_bit 


total_time = len(bit_sequence) / bit_rate
samples_per_bit = 500 // len(bit_sequence)
time = np.linspace(0, total_time, samples_per_bit * len(bit_sequence))  


signal_1 = np.zeros(len(time))
modulated_signal_1 = np.zeros(len(time))


carrier_signal_1 = np.sin(2 * np.pi * carrier_frequency * time)


signal_2 = np.zeros(len(time))
modulated_signal_2 = np.zeros(len(time))


carrier_signal_2 = np.sin(2 * np.pi * carrier_frequency * time + (90 * (np.pi / 180)))

signal_3 = np.zeros(len(time))
sum_signal = []


for i, bit in enumerate(bit_sequence):
    start_index = i * samples_per_bit
    end_index = (i + 1) * samples_per_bit

    
    modulated_signal_1[start_index:end_index] = np.sin(2 * np.pi * carrier_frequency * time[start_index:end_index] + (180 * (np.pi / 180)))

    
    if bit == 1:
        
        modulated_signal_1[start_index:end_index] = np.sin(2 * np.pi * carrier_frequency * time[start_index:end_index] + (0 * (np.pi / 180)))

    
    signal_1[start_index:end_index] = bit


for i, bit in enumerate(bit_sequence_2):
    start_index = i * samples_per_bit
    end_index = (i + 1) * samples_per_bit
    
    modulated_signal_2[start_index:end_index] = np.sin(2 * np.pi * carrier_frequency * time[start_index:end_index] + (260 * (np.pi / 180)))

    if bit == 1:
        modulated_signal_2[start_index:end_index] = np.sin(2 * np.pi * carrier_frequency * time[start_index:end_index] + (90* (np.pi / 180)))

    
    signal_2[start_index:end_index] = bit


fig, axes = plt.subplots(7, 1, figsize=(10, 12), sharex=True)


bit_boundaries = np.linspace(0, total_time, len(bit_sequence) + 1)


axes[0].plot(time, signal_1, color='red', lw=3, label="First Binary Signal")
axes[0].set_ylim([-1.5, 1.5])
axes[0].legend(loc='lower left')
axes[0].grid(True)
axes[0].set_xlim([0, total_time]) 


for boundary in bit_boundaries:
    axes[0].axvline(boundary, color='gray', linestyle='--')


axes[1].plot(time, carrier_signal_1, color='black', lw=1.5, label="Carrier Signal", alpha=0.7)
axes[1].set_ylim([-1.5, 1.5])
axes[1].legend(loc='lower left')
axes[1].grid(True)
axes[1].set_xlim([0, total_time])


for boundary in bit_boundaries:
    axes[1].axvline(boundary, color='gray', linestyle='--')


axes[2].plot(time, modulated_signal_1, color='cyan', lw=2, label="Modulated Signal")
axes[2].set_ylim([-1.5, 1.5])
axes[2].legend(loc='lower left')
axes[2].grid(True)
axes[2].set_xlim([0, total_time]) 


for boundary in bit_boundaries:
    axes[2].axvline(boundary, color='gray', linestyle='--')


axes[3].plot(time, signal_2, color='red', lw=3, label="Second Binary Signal")
axes[3].set_ylim([-1.5, 1.5])
axes[3].legend(loc='lower left')
axes[3].grid(True)
axes[3].set_xlim([0, total_time])


for boundary in bit_boundaries:
    axes[3].axvline(boundary, color='gray', linestyle='--')


axes[4].plot(time, carrier_signal_2, color='black', lw=1.5, label="Second Carrier Signal", alpha=0.7)
axes[4].set_ylim([-1.5, 1.5])
axes[4].legend(loc='lower left')
axes[4].grid(True)
axes[4].set_xlim([0, total_time])


for boundary in bit_boundaries:
    axes[4].axvline(boundary, color='gray', linestyle='--')


axes[5].plot(time, modulated_signal_2, color='cyan', lw=1.5, label="Second Modulated Signal")
axes[5].set_ylim([-1.5, 1.5])
axes[5].legend(loc='lower left')
axes[5].grid(True)
axes[5].set_xlim([0, total_time]) 


for boundary in bit_boundaries:
    axes[5].axvline(boundary, color='gray', linestyle='--')

sum_signal = modulated_signal_1 + modulated_signal_2

axes[6].plot(time, sum_signal, lw=1.5, label="Sum Signal")
axes[6].set_ylim([-1.5, 1.5])
axes[6].legend(loc='lower left')
axes[6].grid(True)
axes[6].set_xlim([0, total_time])

for boundary in bit_boundaries:
    axes[6].axvline(boundary, color='gray', linestyle='--')

axes[-1].set_xticks(bit_boundaries)

axes[-1].set_xlabel('Time (s)')

plt.tight_layout(pad=0)
plt.show()
