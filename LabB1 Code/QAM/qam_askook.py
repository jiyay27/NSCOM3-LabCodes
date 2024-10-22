import numpy as np
import matplotlib.pyplot as plt

# Define the OOK (ASK) constellation points
ook_symbols = {
    '0': 0,   
    '1': 1    
}

def generate_random_bits(num_symbols):
    bits = np.random.randint(0, 2, num_symbols) 
    return bits

def map_bits_to_ook(bits):
    symbols = [ook_symbols[str(bit)] for bit in bits]
    return np.array(symbols)

def plot_ook_constellation(symbols):
    plt.figure(figsize=(6, 6)) 
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.5, 1.5)

    plt.scatter(symbols, np.zeros_like(symbols), color='blue', s=100)  

    for sym, coord in ook_symbols.items():
        plt.text(coord, 0, f'{sym}', fontsize=12, ha='center', va='bottom', color='red')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='lightgray') 
    plt.title('OOK (ASK) Constellation Diagram', color='black') 
    plt.xlabel('Amplitude', color='black') 
    plt.ylabel('Magnitude', color='black') 
    plt.show()

num_symbols = 100  
bits = generate_random_bits(num_symbols)
ook_data = map_bits_to_ook(bits)
plot_ook_constellation(ook_data)
