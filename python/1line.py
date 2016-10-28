#!/usr/bin/env python

import sys

#print '\n'.join([''.join([(sys.argv[1][(x-y)%len(sys.argv[1])] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30,30)]) for y in range(15,-15,-1)])

# The smaller factors of x,y are, the bigger the heart is
print '\n'.join([''.join([('LoveLn'[(x-y)%6]if ((x*0.025)**2+(y*0.05)**2-1)**3-(x*0.025)**2*(y*0.05)**3 <= 0 else ' ')for x in range(-30,30)])for y in range(15,-15,-1)])
