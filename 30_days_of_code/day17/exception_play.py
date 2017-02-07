#!/usr/bin/env python3
#Write your code here
class error(Exception):
    pass

class Calculator:
    def __init__(self):
        self.data = "cat"
    def power(self,num,exp):
    #Complete this method
        if (num < 0 or exp < 0):
            raise RuntimeError('n and p should be non-negative') from error
        else:
            return num**exp

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)
