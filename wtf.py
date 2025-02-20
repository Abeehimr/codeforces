import sys
from collections import defaultdict, deque, Counter
import math
import heapq
import bisect
import random

dfsss,hashingggg = 0,0
def cinput():
    return sys.stdin.readline().rstrip()
def cprint(output):
    sys.stdout.write(output + '\n')
    sys.stdout.flush()
def rint():
    return int(cinput())
def rlist():
    return list(map(int, cinput().split()))
def rstring():
    return cinput()
def ristring():
    return list(map(int,rstring()))
def rcstring():
    s = cinput()
    return(list(s))
def rslist():
    return list(cinput().split())
def rints():
    return list(map(int, cinput().split()))
def plist(lst):
    cprint(" ".join(map(str, lst)))
def print_2d_list(matrix):
    for row in matrix:
        cprint(" ".join(map(str, row)))
if dfsss:
    from types import GeneratorType



    def bootstrap(f, stack=[]):
        def wrappedfunc(*args, **kwargs):
            if stack:
                return f(*args, **kwargs)
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
        return wrappedfunc
    
#rnd = random.randint(x,ys)
if hashingggg:
    RANDOM = random.randrange(2**62)
    def w(x):
        return x ^ RANDOM
inf = 10**18 + 10
testcases = rint()

