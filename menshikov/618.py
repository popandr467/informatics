from itertools import permutations as pm
print('\n'.join(''.join(i) for i in pm(*(lambda s:(s,len(s)))(input()))))