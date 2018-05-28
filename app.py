#!/usr/bin/env python
import sys
import getopt
from helpers import *
from improved import *

try:
    options, remainder = getopt.getopt(sys.argv[1:], 'n:i:')

except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)



for opt, arg in options:
    if opt in ('-n'):
        n = int(arg)


    elif opt in ('-i'):
        i = int(arg)

if len(remainder) > 0:
    if remainder[0].lower() != 'improved':
        print('ERROR: usage "./app.py -m 20 -i 1000 improved"')
        sys.exit(1)
    else:
        simulate_improved(n, i)
        sys.exit(1)

simulate(n, i)













# check valid input: 2 arguments in form of ./app.py n i
# where n=nodes, i=iterations
# OLD
# if len(sys.argv) == 3:
#     try:
#         n = int(sys.argv[1])
#         i = int(sys.argv[2])
#         print(n, i)
#     except Exception as e:
#         print("wrong input, try again")
#
#     simulate(n, i)
#
# else:
#     print("only 2 args allowed")


