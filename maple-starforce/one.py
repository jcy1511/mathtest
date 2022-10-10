from prs import successPrs

result = 1
for s in range(12, 22):
    result *= successPrs[s]/100
result = float(format(result, '.20f'))*100

print(f"{result}%")
