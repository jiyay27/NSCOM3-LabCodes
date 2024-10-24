def calculate_checksum(message):
    checksum = 0

    for char in message:
        ascii_value = ord(char)
        print(f"Character: {char}, ASCII: {ascii_value}")
        checksum += ascii_value

        if checksum > 255:
            checksum = (checksum & 0xFF) + (checksum >> 8)
        # print(f"Current Sum: {checksum}")

    binary_value = bin(checksum)[2:].zfill(8)
    print(f"Binary before MSB and LSB extraction: {binary_value}")

    msb = binary_value[:4]  
    lsb = binary_value[4:] 

    summed_value = (int(msb, 2) + int(lsb, 2)) & 0xF  
    updated_binary_value = bin(summed_value)[2:].zfill(4)  
    print(f"Binary after MSB + LSB addition: {updated_binary_value}")

    complemented_value = ''.join('1' if bit == '0' else '0' for bit in updated_binary_value)
    checksum = int(complemented_value, 2)
    print(f"Binary Complement: {complemented_value} == {checksum}")

    return checksum

def validate_checksum(message, received_checksum):
    recalculated_checksum = calculate_checksum(message)

    total = (recalculated_checksum + received_checksum) & 0xFF

    print(f"Validation Sum: {total}")

    return total == 0

word = "PKA_NSCOM03"
checksum_sender = calculate_checksum(word)

print("\nFinal Checksum:", checksum_sender)
