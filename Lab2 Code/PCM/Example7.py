bandwidth = 200 #kHz
sample_conversion = bandwidth * 1000 #converting kHz to sample
sampling_signal = 2 * sample_conversion #computation of getting the sample multiplied by 2 since it is ran twice.

print(f"{sampling_signal:.8g} samples per second")