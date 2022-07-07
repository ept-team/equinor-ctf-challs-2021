import string
import random 
import os
from pathlib import Path

dir = '/opt/flag'

Path(dir).mkdir(parents=True, exist_ok=True)

for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
 
flag = open('/root/flag.txt').read().strip()

numberOfFiles = 200
filenames = [''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(5,50))) for _ in range(numberOfFiles)]
flagFile = random.randint(0,numberOfFiles-1) 
for i, file  in enumerate(filenames):
    with open(f'{dir}/{file}', 'w') as f:
        if i == flagFile:
            f.write(flag + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(200-len(flag))) + '\n')
        else:
            f.write(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(200)) + '\n')

print('files created.')