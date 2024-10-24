def xor(a, b):
    result = ""
    for i in range(len(b)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

def crc_long_division(message, polynomial):
    message = message + '0' * (len(polynomial) - 1)
    msg_len = len(message)
    poly_len = len(polynomial)
    
    print(f"Initial Message: {message}")
    
    while '1' in message[:msg_len - poly_len + 1]:
        shift = message.index('1')
        before_xor = message[shift:shift + poly_len]
        message = message[:shift] + xor(before_xor, polynomial) + message[shift + poly_len:]
        
        print(f"Shift: {shift}")
        print(f"Before XOR: {before_xor}")
        print(f"After XOR: {xor(before_xor, polynomial)}")
        print(f"Message Now: {message}")
    
    return message[-(poly_len - 1):]

# given
message = "1010011010"
polynomial = "110101"

remainder = crc_long_division(message, polynomial)
print(f"Final Remainder: {remainder}")