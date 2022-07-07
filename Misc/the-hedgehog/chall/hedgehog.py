#!/usr/bin/env python3
import re
import os
import json


def quit(msg):
    print('Anta baka!', msg)
    exit()


def system(cmd):
    print('-'*100)
    os.system(cmd)
    print('-'*100)
    print()


print('Welcome!')
print()
print('So I found this new cool tool called md5sum which allows you to calculate the MD5 hash of any file!')
print('The hash is supposed to be pretty unique and depend on the content. So I guess that would mean given')
print('the hash you should be able to get the content back, right?')
print()
print('I could not figure this out for myself, but maybe you can help. In good faith I have provided you')
print('with some files you can try and play with to see if you read the content:')
system('ls')
print("Here, I'll even open a couple of files for you so that you can compare the content to reverse the")
print("hash or something:")
print('fire:')
system('cat fire')
print('letter:')
system('cat letter')
print('goodguy:')
system('cat goodguy')
print()

files = json.loads(input('Enter files to hash: '))
if type(files) != list or not files:
    quit('This is not a list of files!')
for file in files:
    if type(file) != str:
        quit('This is not a string!')
    if not re.match('^[a-z]+$', file):
        quit("Don't you dare look forward!")

system('md5sum ' + ' '.join(files))
