import numpy as np
import matplotlib.pyplot as plt

f_max = 4000  #assumed max freq

#nyquist
fs = 2 * f_max
duration = 1

t = np.linspace(0, duration, int(fs * duration), endpoint=False)

voice_signal = np.sin(2 * np.pi * f_max * t)

plt.figure(figsize=(10, 4))
plt.plot(t, voice_signal, label='Voice Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Digitized Voice Signal at Nyquist Rate')
plt.legend()
plt.grid(True)
plt.show()
