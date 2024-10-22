import numpy as np
import matplotlib.pyplot as plt

# Define the BPSK constellation points
bpsk_symbols = {
    '1': 1 + 0j,   # Represents the symbol (1, 0) for '0'
    '0': -1 + 0j   # Represents the symbol (-1, 0) for '1'
}

# Generate random bits (0s and 1s)
def generate_random_bits(num_symbols):
    bits = np.random.randint(0, 2, num_symbols)  # 1 bit per symbol
    return bits

# Map the bits to BPSK symbols
def map_bits_to_bpsk(bits):
    symbols = [bpsk_symbols[str(bit)] for bit in bits]
    return np.array(symbols)

# Plot the BPSK constellation
def plot_bpsk_constellation(symbols):
    plt.figure(figsize=(6, 6))  # Default figure size
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)

    plt.scatter(symbols.real, symbols.imag, color='blue', s=100)  # Plotting symbols

    # Adding labels for clarity
    for sym, coord in bpsk_symbols.items():
        plt.text(coord.real, coord.imag, f'{sym}', fontsize=12, ha='center', va='bottom', color='red')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='lightgray')  # Set grid line color to light gray for better visibility
    plt.title('BPSK Constellation Diagram', color='black')  # Title color remains black
    plt.xlabel('In-phase', color='black')  # X-axis label color remains black
    plt.ylabel('Quadrature', color='black')  # Y-axis label color remains black
    plt.show()

# Example usage
num_symbols = 100  # Number of symbols to generate
bits = generate_random_bits(num_symbols)
bpsk_data = map_bits_to_bpsk(bits)
plot_bpsk_constellation(bpsk_data)
