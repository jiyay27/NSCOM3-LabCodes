def calculate_checksum(message):
    checksum = 0

    for char in message:
        ascii_value = ord(char)
        print(f"Character: {char}, ASCII: {ascii_value}")
        checksum += ascii_value

        
        if checksum > 255:
            checksum = (checksum & 0xFF) + (checksum >> 8) 
        print(f"Current Sum (before processing): {checksum}")

        
        binary_value = bin(checksum)[2:].zfill(8)  
        msb = binary_value[:2]  
        rest = binary_value[2:]

       
        updated_binary_value = bin(int(rest, 2) + int(msb, 2))[2:].zfill(6)
        print(f"Binary before complement: {updated_binary_value}")

     
        complemented_value = ''.join('1' if bit == '0' else '0' for bit in updated_binary_value)
        checksum = int(complemented_value, 2)
        print(f"Final Checksum (after complement): {checksum}")

    return checksum

def validate_checksum(message, received_checksum):
    recalculated_checksum = calculate_checksum(message)
    total = (recalculated_checksum + received_checksum) & 0xFF

    
    return total == 0


word = "NSCOM03"
checksum_sender = calculate_checksum(word)
is_valid = validate_checksum(word, checksum_sender)

print("\nFinal Checksum (Sender):", checksum_sender)
print("Is the checksum valid at receiver:", is_valid)
