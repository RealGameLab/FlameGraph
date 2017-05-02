# -*- coding: UTF-8 -*- 

import re
import sys

if len(sys.argv) < 2:
    print('Useage: python stackcollapse-unreal.py filename')
    exit(1)

filename = sys.argv[1] 

stack = []
toptime = 0

with open(filename, 'r') as file:
    for line in file:
        m = re.match(r'[\S ]*LogStats: ( *)(\d*.\d{3})ms \( *\d*\)  -  ([\w :/.]+)', line)
        if m:
            deep, time, name = m.groups()
            time = int(float(time) * 1000)
            deep = int(len(deep) / 2)
            name = name.strip()

            if len(stack) >= deep:
                print('%s %d' % (';'.join(stack), toptime))
                stack = stack[:deep - 1]

            while len(stack) < deep - 1:
                stack.append('unknown')
            
            stack.append(name)
            toptime = time

    # print the last    
    print('%s %d' % (';'.join(stack), toptime))
