import numpy as np
import matplotlib.pyplot as plt

# Define the BPSK constellation points
bpsk_symbols = {
    '1': 1 + 0j,  
    '0': -1 + 0j   
}

def generate_random_bits(num_symbols):
    bits = np.random.randint(0, 2, num_symbols) 
    return bits

def map_bits_to_bpsk(bits):
    symbols = [bpsk_symbols[str(bit)] for bit in bits]
    return np.array(symbols)

def plot_bpsk_constellation(symbols):
    plt.figure(figsize=(6, 6))
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)

    plt.scatter(symbols.real, symbols.imag, color='blue', s=100)

    
    for sym, coord in bpsk_symbols.items():
        plt.text(coord.real, coord.imag, f'{sym}', fontsize=12, ha='center', va='bottom', color='red')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='lightgray') 
    plt.title('BPSK Constellation Diagram', color='black') 
    plt.xlabel('In-phase', color='black')  
    plt.ylabel('Quadrature', color='black') 
    plt.show()


num_symbols = 100  
bits = generate_random_bits(num_symbols)
bpsk_data = map_bits_to_bpsk(bits)
plot_bpsk_constellation(bpsk_data)
