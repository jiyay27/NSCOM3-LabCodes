def calculate_checksum(message):
    checksum = 0

    for char in message:
        ascii_value = ord(char)
        print(f"Character: {char}, ASCII: {ascii_value}")
        checksum += ascii_value

        if checksum > 255:
            checksum = (checksum & 0xFF) + (checksum >> 8)
        print(f"Current Sum: {checksum}")

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
    checksum = 0
    
    for char in message:
        ascii_value = ord(char)
        print(f"Character: {char}, ASCII: {ascii_value}")
        checksum += ascii_value

        if checksum > 255:
            checksum = (checksum & 0xFF) + (checksum >> 8)

    checksum += received_checksum

    binary_value = bin(received_checksum)[2:].zfill(8)
    print(f"Binary before MSB and LSB extraction: {binary_value}")

    msb = binary_value[:4]
    lsb = binary_value[4:]


    summed_value = (int(msb, 2) + int(lsb, 2)) & 0xF
    updated_binary_value = bin(summed_value)[2:].zfill(4)
    print(f"Binary after MSB + LSB addition: {updated_binary_value}")

    complemented_value = ''.join('1' if bit == '0' else '0' for bit in updated_binary_value)
    checksum = int(complemented_value, 2)
    print(f"Binary Complement: {complemented_value} == {received_checksum}")

    return checksum


print("=== Sender ===")
word = "hi"
checksum_sender = calculate_checksum(word)
print(f"\nFinal Sender Checksum: {checksum_sender}")


print("\n=== Receiver ===")
if validate_checksum(word, checksum_sender):
    print("Checksum is valid. The sender and receiver checksums match.")
else:
    print("Checksum is invalid. There is a mismatch between sender and receiver.")
