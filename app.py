#!/usr/bin/env python
import sys
from helpers import *

# check valid input: 2 arguments in form of ./app.py n i
# where n=nodes, i=iterations
if len(sys.argv) == 3:
    try:
        n = int(sys.argv[1])
        i = int(sys.argv[2])
        print(n, i)
    except Exception as e:
        print("wrong input, try again")

    simulate(n, i)

else:
    print("only 2 args allowed")


