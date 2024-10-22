import numpy as np
import matplotlib.pyplot as plt

# Define the OOK (ASK) constellation points
ook_symbols = {
    '0': 0,   # Represents the symbol (0)
    '1': 1    # Represents the symbol (1)
}

# Generate random bits (0s and 1s)
def generate_random_bits(num_symbols):
    bits = np.random.randint(0, 2, num_symbols)  # 1 bit per symbol
    return bits

# Map the bits to OOK symbols
def map_bits_to_ook(bits):
    symbols = [ook_symbols[str(bit)] for bit in bits]
    return np.array(symbols)

# Plot the OOK constellation
def plot_ook_constellation(symbols):
    plt.figure(figsize=(6, 6))  # Default figure size
    plt.xlim(-0.5, 1.5)
    plt.ylim(-0.5, 1.5)

    plt.scatter(symbols, np.zeros_like(symbols), color='blue', s=100)  # Plotting symbols on the x-axis

    # Adding labels for clarity
    for sym, coord in ook_symbols.items():
        plt.text(coord, 0, f'{sym}', fontsize=12, ha='center', va='bottom', color='red')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='lightgray')  # Set grid line color to light gray for better visibility
    plt.title('OOK (ASK) Constellation Diagram', color='black')  # Title color remains black
    plt.xlabel('Amplitude', color='black')  # X-axis label color remains black
    plt.ylabel('Magnitude', color='black')  # Y-axis label color remains black
    plt.show()

# Example usage
num_symbols = 100  # Number of symbols to generate
bits = generate_random_bits(num_symbols)
ook_data = map_bits_to_ook(bits)
plot_ook_constellation(ook_data)
