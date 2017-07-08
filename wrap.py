import itertools
from statistics import stdev

string = "When, in the course of human events, it becomes necessary"
string = "We the people of the United States, in order to form a more perfect union, establish justice, insure domestic tranquility"

top_how_many = 1
max_newlines = 6

def pretty(LoL):
    S = ''
    for r in LoL:
        S = S + str(round(r[0], 2)) + ' :\n' + r[1] + '\n\n'
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

for num_newlines in range(1, max_newlines):

    bits = string.count(' ')
    args = tuple(itertools.repeat((0,1), bits))
    bitmaps = itertools.product(*args)

    print(str(num_newlines) + '\n========\n')
    pairs = []
    for b in bitmaps:
        if sum(b) == num_newlines:
            words = string.split()
            wrapped = all_join(words[1:], words[0], b)
            lengths = [len(line) for line in wrapped.split('\n')]
            pairs.append([stdev(lengths), wrapped])
    pairs.sort(key=lambda e: e[0])
    print(pretty(pairs[0:top_how_many]))
