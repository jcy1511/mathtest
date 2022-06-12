from sequence import *

a = Sequence()
a.setDataBySeq([2, 8, 32, 128])
r = a.cr
a.info()
print("")

b = Sequence()
b.setDataBySn("n**2 + 2*n")
b.info()
print("")

print("답 :", b.a(r))
