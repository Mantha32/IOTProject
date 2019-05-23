import base64
import binascii
import dateutil.parser

# Decode an uplink message payload from a buffer
# From base64 payload to hex to string decoder
def decoder(payload):
    messageByte = base64.b64decode(payload)
    return messageByte.decode('utf-8')

# Convert bytes in hexadecimal to string
def hex_to_string(payload):
    byte_to_string = binascii.hexlify(bytearray(payload))
    return byte_to_string.decode('utf-8', 'strict')


# Convert ISO datetime to datetime.datetime
def iso_to_datetime(dtr_str):
    return dateutil.parser.parse(dtr_str)
