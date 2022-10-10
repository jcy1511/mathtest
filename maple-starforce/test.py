from itertools import *
whole = [i for i in range(12, 14)]
everyFailList = list(combinations_with_replacement(whole, 2))
print(everyFailList)
