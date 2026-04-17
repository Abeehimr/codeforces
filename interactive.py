import sys
def ask(a,b):
    print(f'? {a} {b}')
    sys.stdout.flush()
    o = int(input().strip())
    if o == -1: quit()
    return o
