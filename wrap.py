import itertools
from statistics import stdev

string = "When, in the course of human events, it becomes necessary"
bits = string.count(' ')
words = string.split()

args = tuple(itertools.repeat((0,1), bits))
bitmaps = itertools.product(*args)

def pretty(LoL):
    S = ''
    for r in LoL:
        for e in r:
            S = S + str(e) + '\n'
        S = S + '\n'
    return S

def all_join(L, S, bitmap):
    assert len(L) == len(bitmap)
    if len(L) == 0 or len(bitmap) == 0:
        return S
    if bitmap[0]:
        c = '\n'
    else:
        c = ' '
    bitmap = bitmap[1:]
    e = L[0]
    L = L[1:]
    S = S + c + e
    return all_join(L, S, bitmap)

####

num_newlines = 2

pairs = []
for b in bitmaps:
    if sum(b) == num_newlines:
        wrapped = all_join(words[1:], words[0], b)
        lengths = [len(line) for line in wrapped.split('\n')]
        pairs.append([stdev(lengths), wrapped])
pairs.sort(key=lambda e: e[0])
print(pretty(pairs[0:4]))