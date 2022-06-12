from __future__ import print_function
import sympy as sp


def setDataBySn(sn):
    n = sp.Symbol('n')
    Sn = sp.sympify(sn)
    Sn1 = Sn.subs(n, n-1)
    an = sp.expand(Sn - Sn1)

    if an.subs(n, 1) == Sn.subs(n, 1):
        return an
    else:


print(setDataBySn("n**2+2*n"))
