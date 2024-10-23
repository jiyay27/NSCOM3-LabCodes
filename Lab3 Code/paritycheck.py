def parity_check(binary_sequence):
    # Count the number of 1's in the binary sequence
    ones_count = binary_sequence.count(1)    

    if ones_count % 2 == 0:
        return 1 # even parity
    else:
        return 0 # odd parity


def even_parity_sender(binary_sequence, parity):
    if (parity == 0):
        binary_sequence.append(1) # append 1 if there are odd no. of 1
    else:
        binary_sequence.append(0) # append 0 if there are even no. of 1

    return binary_sequence


def even_parity_receiver(binary_sequence):
    # check if the parity sequence is even
    bin_count = binary_sequence.count(1)

    if (bin_count % 2 == 0):
        return "No" # even count of 1s received, no error
    else:
        return "Yes" # odd count of 1s received, error


def swap_middle_elements(binary_sequence): # to simulate error when receiving
    n = len(binary_sequence)

    # check if the array is even or odd
    if n % 2 == 0:
        mid_ind1 = n // 2 - 1  
        mid_ind2 = n // 2 

        # Swap the two middle elements
        binary_sequence[mid_ind1], binary_sequence[mid_ind2] = binary_sequence[mid_ind2], binary_sequence[mid_ind1]
    
    return binary_sequence


print(f"\nScenario 1: No Error Received\n")

bin_sequence = [1,0,1,1,0,0,0]
print(f"Orginal Sequence: {bin_sequence}\n")


# checks bit sequence to send and adds parity
parity = parity_check(bin_sequence)
parity_bin_sequence = even_parity_sender(bin_sequence, parity)

print(f"Partity Sent:     {parity_bin_sequence}")

parity_reply = even_parity_receiver(parity_bin_sequence)

print(f"Partity Received: {parity_bin_sequence}")
print(f"Is there an Error?: {parity_reply}\n")
    

print(f"\nScenario 2: Error Received - Undetected\n")

bin_sequence = [1,0,1,1,0,0,0]
print(f"Orginal Sequence: {bin_sequence}\n")


# checks bit sequence to send and adds parity
parity = parity_check(bin_sequence)
parity_bin_sequence = even_parity_sender(bin_sequence, parity)

print(f"Partity Sent:     {parity_bin_sequence}")

# received bits are error but undetected
parity_bin_sequence = swap_middle_elements(parity_bin_sequence)
parity_reply = even_parity_receiver(parity_bin_sequence)

print(f"Partity Received: {parity_bin_sequence}")
print(f"Is there an Error?: {parity_reply}\n")


print(f"\nScenario 3: Error Received - Detected\n")

bin_sequence = [1,0,1,1,0,0,0]
print(f"Orginal Sequence: {bin_sequence}\n")


# checks bit sequence to send and adds parity
parity = parity_check(bin_sequence)
parity_bin_sequence = even_parity_sender(bin_sequence, parity)

print(f"Partity Sent:     {parity_bin_sequence}")

# received bits are error but undetected
parity_bin_sequence.pop()
parity_bin_sequence.pop()
parity_bin_sequence.append(1)
parity_bin_sequence.append(1)
parity_reply = even_parity_receiver(parity_bin_sequence)

print(f"Partity Received: {parity_bin_sequence}")
print(f"Is there an Error?: {parity_reply}\n")