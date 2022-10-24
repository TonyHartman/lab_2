import itertools as it
s = '0123456789ab'
s1 = '01234'
per = list(it.permutations(s, 5))
per1 = list(it.permutations(s1, 5))
print(len(per) // len(per1))
