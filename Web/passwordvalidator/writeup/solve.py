from z3 import *


def main():
    length = 12
    flag = [BitVec('c' + str(i), length)  for i in range(length)]
    
    s = Solver()

    for i in range(length):    
        s.add(And(flag[i] >= 33,flag[i] <= 126)) 
        

    for i in range(length):
        for j in range(i+1,length,1):
            s.add(flag[i] != flag[j])
    expr = [And(flag[i] >= ord('a'), flag[i] <= ord('z')) for i in range(length)] 
    expr1 = [And(flag[i] >= ord('A'), flag[i] <= ord('Z')) for i in range(length)]     
    expr2 = [And(flag[i] >= ord('0'), flag[i] <= ord('9')) for i in range(length)]  
    expr3 = [Or(
        And(flag[i] >= ord(' '), flag[i] <= ord('/')),
        And(flag[i] >= ord(':'), flag[i] <= ord('@')),
        And(flag[i] >= ord('['), flag[i] <= ord('`')),
        And(flag[i] >= ord('{'), flag[i] <= ord('~'))
        ) for i in range(length)]
    
    s.add( z3.PbGe([(x,1) for x in expr], 3) )
    s.add( z3.PbGe([(x,1) for x in expr1], 3) )
    s.add( z3.PbGe([(x,1) for x in expr2], 3) )
    s.add( z3.PbGe([(x,1) for x in expr3], 3) )


    s.add((flag[0] + flag[1]) ^flag[2] == 0xde)
    s.add((flag[3] + flag[4]) ^flag[5] == 0xad)
    s.add((flag[6] + flag[7]) ^flag[8] == 0xc0)
    s.add((flag[9] + flag[10]) ^flag[11] == 0xde)

    while s.check() == sat:
        m = s.model()
        
        a = bytes(map(lambda x: m[x].as_long(), flag)).decode()
        print(a)

if __name__ == '__main__':
    main()


