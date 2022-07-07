#!/usr/bin/env python3
import time
import random
import sys


def write(line, finalSleep=1.5):
    for c in line:
        if not c.isalpha():
            time.sleep(0.07)
        print(c, end="")
        time.sleep(random.uniform(0.040, 0.070))
    time.sleep(finalSleep)
    print()


def die(blacklist):
    write('Did you...')
    write('Did you seriously?!')
    write('Did you seriously just do that!?!')
    write('Like..')
    write('Why....')
    write('Why would you do such a thing?')
    write('I thought I could trust you...')
    write("It is always the same thing...")
    write('As soon as I show you ANY amount of TRUST')
    write('You just come here and ruin everything...')
    write('Like...')
    write('I thought we had a nice thing going??')
    write('You, providing nice clean python code')
    write('And me executing it')
    write('Simple as that...')
    write('But nooooooooooo....')
    write('Here you try to run that ugly, dirty code of yours')
    write('Causing me to have to sort to fricking BLACKLISTS to stop you!?')
    write(f'Had it not been for me defining my blacklist as {blacklist=} and removing all the __builtins__')
    write('Then you could have done some serious damage there')
    write('Well...')
    write('I guess that is goodbye then...')
    write('Also, if you really need it, you can type "__source"')
    write('exit(1)', 0)
    exit(1)


def run(src, locals):
    if src == '__source':
        print(open(sys.argv[0]).read())
        exit()

    blacklist = ['__', 'import']
    if any(b in src for b in blacklist):
        die(blacklist)
    co = compile(src, "kjell", "single")
    eval(co, {'__builtins__': {}}, locals)


locals = {}
while True:
    run(input('> '), locals)
