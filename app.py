#!/usr/bin/env python
import sys
import getopt
from helpers import *
from improved import *

'''USE ./app.py -n 20 -i 1000 OR ./app.py -n 20 -i 1000 improved'''

# check valid input
try:
    options, remainder = getopt.getopt(sys.argv[1:], 'n:i:')

except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)


for opt, arg in options:
    if opt in ('-n'):
        try:
            n = int(arg)
        except:
            print("ERROR: only integers")
            sys.exit(1)


    elif opt in ('-i'):
        try:
            i = int(arg)
        except:
            print("ERROR: only integers")
            sys.exit(1)

    else:
        print("ERROR: only integers")
        sys.exit(1)

if len(remainder) > 0:
    if remainder[0].lower() != 'improved':
        print('ERROR: usage "./app.py -m 20 -i 1000 improved"')
        sys.exit(1)
    else:
        simulate_improved(n, i)
        sys.exit(1)

if len(sys.argv) < 3:
    print('ERROR: usage "./app.py -m 20 -i 1000"')
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


