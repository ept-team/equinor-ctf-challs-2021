import time
import random
import math
import base64
import binascii
import os
import threading

CODE = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}

flag = open("flag.txt", "r").read()

operators = ["-", "+", "*", "/"]
words = ["parser","suggestivenesses","pigments","uncontrastive","rusky","adulthood","participating","parked","biotically","blushing","lazylegs","nondeclaration","packaging","peppery","superweapons","unprincipal","chinless","unconsolatory","appalling","electropotential","tearstained","athletical","unpraiseful","notifying","honer","status","outcompete","overprases","tradesman","unbiased","impersonify","blackness","protanomaly","pinkfish","excommunicative","assistant","beading","allergy","insaturable","skelms","smokish","impartable","goddaughters","disrespect","unpile","originates","overnarrowly","wreathing","reconfiscate","electively","flittering","ravery","shaftman","physicological","positivistically","oversell","snowbelt","outdevil","misclaimed","open-caisson","conductility"]
count = 0

def evaluate(string1, string2):
	global count
	if str(string1) == str(string2):
		print("Correct!", flush=True)
		count += 1
		reset_time()

	else:
		print("Wrong! Better luck next time.", flush=True)
		os._exit(1)

def reset_time():
	global time_limit
	global start_time
	time_limit = 5
	start_time = time.time()

def calcMorse(word):
	word = word.upper()
	encodedWord = ""
	for character in word:
		encodedWord += CODE[character] + " " 
	return encodedWord

def math():
	correct = 0
	while correct == 0:
		num1 = random.randint(1, 20)
		num2 = random.randint(1, 20)
		equation = str(num1) + " " + random.choice(operators) + " " + str(num2)
		correct= int((eval(equation)))

	print(f"Calculate the following equation (ignore decimals): {equation} ", flush=True)
	answer = str(input())
	evaluate(answer, correct)

def morse():
	word = random.choice(words)
	morse = calcMorse(word)
	print("Decode the following morse code: " + morse, flush=True)

	answer = str(input()).lower()
	evaluate(answer, word)

def decodeHex():
	word = random.choice(words)
	encoded = word.encode("ascii")
	encoded = binascii.hexlify(encoded).decode()
	print("Decode the following hexadecimals: " + encoded, flush=True)

	answer = str(input())
	evaluate(answer, word)

def decodeB64():
	word = random.choice(words)
	encoded = word.encode("ascii")
	encoded = base64.b64encode(encoded).decode("ascii")
	print("Decode the following Base64: " + encoded, flush=True)

	answer = str(input())
	evaluate(answer, word)

def ascii():
	word = random.choice(words)
	asc = ""
	for x in word:
		asc += (str(ord(x)) + " ")

	print("Convert the following ascii numbers to a word: " + asc, flush=True)
	answer = str(input())
	evaluate(answer, word)

def start():
	t2 = threading.Thread(target=timing)
	t2.start()
	while count < 100:
		num = random.randint(1, 5)
		if num == 1:
			math()
		elif num == 2:
			morse()
		elif num == 3:
			decodeHex()
		elif num == 4:
			decodeB64()
		elif num == 5:
			ascii()
	
	print(flag, flush=True)
	os._exit(1)

def timing():
	global time_taken
	global start_time
	time_limit = 5
	start_time = time.time()
	while True:
		time_taken = time.time() - start_time
		if time_taken > time_limit:
			print("The time is up!",flush=True)
			os._exit(1)

print("Lets play a game! Answer 100 questions correctly and you will recieve a flag.\nHowever, there is a catch. You only have 5 seconds to answer each question.\nAre you ready?", flush=True)
t = input()
t1 = threading.Thread(target=start)
t1.start()