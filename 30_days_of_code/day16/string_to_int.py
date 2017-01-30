#!/usr/bin/env python3

import sys


S = input().strip()

try:
    i = int(S)
    print (i)
except ValueError:
    #Handle the exception
    print ('Bad String')
