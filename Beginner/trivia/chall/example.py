#If you do not have pwntools installed, run the following command: python3 -m pip install --upgrade pwntools
from pwn import *

#Needs to be implemented
def decodeMorse(morse):
	return morse

#Connect with netcat
io = connect("io.ept.gg", 30023)

#Recieve data
data = io.recvuntil("Are you ready?").decode()
print(data)

#Send data
io.sendline("Yes")

#Recieve empty line then the line containing the question
io.recvline()
question = io.recvline().decode().strip()

#Check if it is a morse question and if so, extract the morse code
if "morse" in question:
	morse = question.split(": ")[1]

	decoded = decodeMorse(morse)
	print(decoded)
	io.sendline(decoded)

io.interactive()