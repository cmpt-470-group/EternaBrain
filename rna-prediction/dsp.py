import numpy as np
from eterna_utils import get_pairmap_from_secstruct
import RNA

def encode_struc(dots):
    s = []
    for i in dots:
        if i == '.':
            s.append(1)
        elif i == '(':
            s.append(2)
        elif i == ')':
            s.append(3)
    return s

def find_parens(s):
    toret = {}
    pstack = []

    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret

dot_bracket = '...((....))(((....)))...'
seq_str = 'A'*len(dot_bracket)
seq = list(seq_str)

current_struc,_ = RNA.fold(seq_str)
target_struc = encode_struc(dot_bracket)
target_pm = get_pairmap_from_secstruct(dot_bracket)
current_pm = get_pairmap_from_secstruct(current_struc)

pairs = find_parens(dot_bracket)

print target_pm
print current_pm

for base1,base2 in pairs.iteritems(): # corrects incorrect base pairings
    print base1,base2
    if (seq[base1] == 'A' and seq[base2] == 'U') or (seq[base1] == 'U' and seq[base2] == 'A'):
        continue
    elif (seq[base1] == 'G' and seq[base2] == 'U') or (seq[base1] == 'U' and seq[base2] == 'G'):
        continue
    elif (seq[base1] == 'G' and seq[base2] == 'C') or (seq[base1] == 'C' and seq[base2] == 'G'):
        continue
    elif (seq[base1] == 'G' and seq[base2] == 'A'):
        seq[base1] = 'U'
    elif (seq[base1] == 'A' and seq[base2] == 'G'):
        seq[base1] = 'C'
    elif (seq[base1] == 'C' and seq[base2] == 'U'):
        seq[base1] = 'A'
    elif (seq[base1] == 'U' and seq[base2] == 'C'):
        seq[base1] = 'G'
    elif (seq[base1] == 'A' and seq[base2] == 'C'):
        seq[base1] = 'G'
    elif (seq[base1] == 'C' and seq[base2] == 'A'):
        seq[base1] = 'U'
    elif (seq[base1] == 'A' and seq[base2] == 'A'):
        seq[base1] = 'U'
    elif (seq[base1] == 'U' and seq[base2] == 'U'):
        seq[base1] = 'A'
    elif (seq[base1] == 'G' and seq[base2] == 'G'):
        seq[base1] = 'C'
    elif (seq[base1] == 'C' and seq[base2] == 'C'):
        seq[base1] = 'G'

print ''.join(seq)

for i in range(len(target_pm)):
    if target_pm[i] == -1:
        seq[i] = 'A'
    else:
        continue

for i in range(len(dot_bracket)):
    if dot_bracket[i] == '(':
        print dot_bracket[i]
        if dot_bracket[i-1] == '.' or dot_bracket[i-1] == ')' or dot_bracket[i+1] == '.' or dot_bracket[i+1] == ')':
            print i
            if (seq[i] == 'G' and seq[pairs[i]] == 'C') or (seq[i] == 'C' and seq[pairs[i]] == 'G'):
                continue
            else:
                seq[i] = 'G'
                seq[pairs[i]] = 'C'


print ''.join(seq)
