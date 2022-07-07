import struct
line = 'P5[a48DbfA@_'
n = 3
a = struct.unpack(">I", bytes(map(lambda l: l[0] + l[1] ^ l[2], [list(map(ord, line))[i:i+3] for i in range(0, len(line), 3)])))[0]

print(hex(a))