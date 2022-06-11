class Sequence:

    def __init__(self, seq):
        self.seq = seq
        self.type = "null"
        self.cd = "공차를 구할 수 없습니다"
        self.cr = "공비를 구할 수 없습니다"

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
            self.cd = self.seq[1]-self.seq[0]
        elif self.type == "등비수열":
            self.cr = self.seq[1]/self.seq[0]

    def a(self, n):
        if self.type == "등차수열":
            return self.seq[0] + (n-1)*(self.seq[1]-self.seq[0])

        elif self.type == "등비수열":
            return self.seq[0] * (self.seq[1]/self.seq[0])**(n-1)

        else:
            return "수열의 일반항을 정의할 수 없습니다"

    def s(self, n):
        sum = 0
        for i in range(n):
            sum += self.seq[i]

        return sum
