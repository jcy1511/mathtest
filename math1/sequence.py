import sympy as sp


class Sequence:

    def __init__(self):
        self.type = "null"
        self.an = "null"
        self.cd = "null"
        self.cr = "null"

    def setDataBySeq(self, seq):
        self.seq = seq

        for i in range(len(seq)-2):
            if self.seq[i+1]*2 == self.seq[i]+self.seq[i+2]:
                self.type = "등차수열"
                continue
            else:
                self.type = "null"
                break

        if self.type != "등차수열":
            for i in range(len(seq)-2):
                if self.seq[i+1]**2 == self.seq[i]*self.seq[i+2]:
                    self.type = "등비수열"
                else:
                    self.type = "null"
                    break

        if self.type == "등차수열":
            self.an = sp.expand(sp.sympify(
                f"{self.seq[0]}+(n-1)*{self.seq[1]-self.seq[0]}"))
            self.getCdOrCr()
        elif self.type == "등비수열":
            self.an = sp.expand(sp.sympify(
                f"{self.seq[0]}*{self.seq[1]/self.seq[0]}**(n-1)"))
            self.getCdOrCr()
        else:
            print("수열의 일반항을 정의할 수 없습니다.")

    def getCdOrCr(self):
        n = sp.Symbol('n')

        if self.an.subs(n, 1)*2 == self.an.subs(n, 0)+self.an.subs(n, 2):
            self.type = "등차수열"
            self.cd = float(self.an.subs(n, 1)-self.an.subs(n, 0))

        elif self.an.subs(n, 1)**2 == self.an.subs(n, 0)*self.an.subs(n, 2):
            self.type = "등비수열"
            self.cr = float(self.an.subs(n, 1)/self.an.subs(n, 0))

    def setDataByAn(self, an):
        self.an = sp.sympify(an)
        self.getCdOrCr()

    def setDataBySn(self, sn):
        n = sp.Symbol('n')
        Sn = sp.sympify(sn)
        Sn1 = Sn.subs(n, n-1)
        an = sp.expand(Sn - Sn1)

        if an.subs(n, 1) == Sn.subs(n, 1):
            self.an = an
        else:
            print(f"a1 = {an.subs(n, 1)}, an = {an} (a>=2)")
            self.an = an
        self.getCdOrCr()

    def a(self, nn):
        n = sp.Symbol('n')
        return float(self.an.subs(n, nn))

    def s(self, nn):
        n = sp.Symbol('n')
        sum = 0
        for i in range(nn):
            sum += self.an.subs(n, i+1)

        return float(sum)

    def info(self):
        print("an =", self.an)
        if self.type == "등차수열":
            print("종류 : 등차수열")
            print("공차 =", self.cd)
        elif self.type == "등비수열":
            print("종류 : 등비수열")
            print("공비 =", self.cr)


a = Sequence()
a.setDataBySeq([1, 3, 5])
print(a.a(2))
a.info()
