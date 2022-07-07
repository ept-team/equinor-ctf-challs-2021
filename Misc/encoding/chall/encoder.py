from datetime import datetime
from random import Random
from time import time

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

ALPHABET = 'abcdefghijklmnopqrstuvwxyz+ABCDEFGHIJKLMNOPQRSTUVWXYZ/0123456789'
def special_encoding(word, count):
    b = Random()
    b.seed(int(time() * 1000))
    if count:
        a = ''.join(b.sample(ALPHABET,len(ALPHABET)))
    else:
        a = ALPHABET
    encoded = ''
    for x in chunks("".join([bin(int(byte)).lstrip('0b').zfill(8) for byte in word.encode("ascii")]), 24):
        y = list(chunks(x, 6))
        for value in y:
            encoded += a[int(value.ljust(6, "0"), 2)]
    print(f"{datetime.fromtimestamp(int(time()))} - Decode the following: {encoded}", flush=True)
