successPrs = []

for s in range(3):
    successPrs.append(95-5*s)
for s in range(3, 15):
    successPrs.append(100-5*s)
for s in range(15, 22):
    successPrs.append(30)
successPrs += [3, 2, 1]

destroyPrs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.6, 1.3,
              1.4, 2.1, 2.1, 2.1, 2.8, 2.8, 7.0, 7.0, 19.4, 29.4, 39.6]

failPrs = [100-successPrs[i]-destroyPrs[i] for i in range(25)]
