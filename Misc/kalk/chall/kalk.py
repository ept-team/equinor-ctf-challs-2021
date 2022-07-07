#!/usr/bin/env python3
import dis
import os


class Math(dict):
    def __init__(self):
        self.e = 0
        self.pi = 0


def kalk(src, locals):
    if '=' in src:
        co = compile(src, "kalk", "single")
        for opc in dis.get_instructions(co):
            if opc.opname not in ['LOAD_NAME', 'LOAD_CONST', 'STORE_NAME', 'STORE_ATTR', 'RETURN_VALUE']:
                print("Bonk! >.<", opc.opname)
                return
        eval(co, {}, locals)
    else:
        co = compile(src, "kalk", "eval")
        for opc in dis.get_instructions(co):
            if 'CALL' in opc.opname:
                print('No U! >.<')
                return

        _ = eval(co, {}, locals | {'math': Math(), 'tease': os.system})
        locals['_'] = _
        return _


locals = {}
while True:
    r = kalk(input('> '), locals)
    if r is not None:
        print(repr(r))
