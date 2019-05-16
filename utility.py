import base64
import binascii

# Decode an uplink message payload from a buffer
# From base64 payload to hex to string decoder
def decoder(payload):
    messageByte = base64.b64decode(payload)
    return messageByte.decode('utf-8')

# Convert bytes in hexadecimal to string
def hex_to_string(payload):
    byte_to_string = binascii.hexlify(bytearray(payload))
    return byte_to_string.decode('utf-8', 'strict')

def timestampConverter(msg):
    print("timestamp:", msg.metadata.time)

# Create device from device object from ttn tier

