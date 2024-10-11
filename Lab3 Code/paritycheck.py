def parity_check(binary_sequence):
    # Count the number of 1's in the binary sequence
    ones_count = binary_sequence.count('1')    

    # Determine parity
    if ones_count % 2 == 0:
        return 1 # even parity
    else:
        return 0 # odd parity
    
def even_parity_sender(binary_sequence, parity):
    # 1 = even, 0 = odd
    if (parity == 0):
        binary_sequence += '1' # append 1 if there are odd no. of 1
    else:
        binary_sequence += '0' # append 0 if there are even no. of 1

    return binary_sequence

def even_parity_receiver(binary_sequence):
    # check if the parity sequence is even
    bin_count = binary_sequence.count('1')

    if (bin_count % 2 == 0):
        return 
    return 0


bin_sequence = "1011000"
parity = parity_check(bin_sequence)
parity_bin_sequence = even_parity_sender(bin_sequence, parity)

print(parity_bin_sequence)

even_parity_receiver(parity_bin_sequence)

print(bin_sequence)
    