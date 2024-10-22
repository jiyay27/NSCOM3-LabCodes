import numpy as np
import matplotlib.pyplot as plt

# Define the 4-QAM constellation points
qam_symbols = {
    '00': -1 - 1j, 
    '01': -1 + 1j,
    '10':  1 - 1j,
    '11':  1 + 1j 
}

def generate_random_bits(num_symbols):
    bits = np.random.randint(0, 2, num_symbols * 2) 
    return bits

def map_bits_to_qam(bits):
    symbols = []
    for i in range(0, len(bits), 2):
        bit_pair = f'{bits[i]}{bits[i+1]}'
        symbols.append(qam_symbols[bit_pair])
    return np.array(symbols)

def plot_qam_constellation(symbols):
    plt.figure(figsize=(6, 6))
    plt.scatter(symbols.real, symbols.imag, color='blue')
    
    for sym, coord in qam_symbols.items():
        plt.text(coord.real, coord.imag, f'{sym}', fontsize=12,
                 ha='center', va='center', color='red')
    
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.title('4-QAM Constellation Diagram')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.xlabel('In-phase')
    plt.ylabel('Quadrature')
    plt.show()

num_symbols = 100
bits = generate_random_bits(num_symbols)
qam_data = map_bits_to_qam(bits)
plot_qam_constellation(qam_data)
