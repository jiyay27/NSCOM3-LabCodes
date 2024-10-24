import binascii

def crc32(data):
    return binascii.crc32(data) & 0xffffffff

message = "1010011010"

# binary to bytes
message_bytes = int(message, 2).to_bytes((len(message) + 7) // 8, byteorder='big')

crc_result = crc32(message_bytes)
print(f"CRC-32 Result: {crc_result:08x}")
