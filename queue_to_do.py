from operator import xor

def help(n):
    ff = [n, 1, n+1, 0]
    return ff[n%4]

def answer(start, length):
    c = 0
    h = length - 1
    for i in range(length):
        c = xor(c, xor(help(start + i*length + h - i), help(start + i*length - 1)))
    return c
