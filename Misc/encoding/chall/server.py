import time
import os
import threading
from random import Random
from encoder import special_encoding

flag = open("flag.txt", "r").read()

words = ["parser","suggestivenesses","pigments","uncontrastive","rusky","adulthood","participating","parked","biotically","blushing","lazylegs","nondeclaration","packaging","peppery","superweapons","unprincipal","chinless","unconsolatory","appalling","electropotential","tearstained","athletical","unpraiseful","notifying","honer","status","outcompete","overprases","tradesman","unbiased","impersonify","blackness","protanomaly","pinkfish","excommunicative","assistant","beading","allergy","insaturable","skelms","smokish","impartable","goddaughters","disrespect","unpile","originates","overnarrowly","wreathing","reconfiscate","electively","flittering","ravery","shaftman","physicological","positivistically","oversell","snowbelt","outdevil","misclaimed","conductility"]
count = 0

a = Random()

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

def decode_me():
	word = a.choice(words)
	special_encoding(word, count)
	answer = str(input())
	evaluate(answer, word)

def start():
	t2 = threading.Thread(target=timing)
	t2.start()
	while count < 100:
			decode_me()
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

print("Someone created an encoding scheme, and now we have trouble decoding the output. Can you help us out? You have 5 seconds per word. All words are lowercase ascii before encoding.\nAre you ready?", flush=True)
t = input()
t1 = threading.Thread(target=start)
t1.start()