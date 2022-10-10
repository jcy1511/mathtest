from prs import successPrs, failPrs
from itertools import *

whole = [i for i in range(12, 22)]

for n in range(1, 21):
    final_result = 0
    i_result = 0          # i번 실패하고 성공할 확률

    for i in range(n+1):
        everyFailList = list(combinations_with_replacement(whole, i))
        for failList in everyFailList:
            result = 1
            successList = [s for s in whole if s not in failList]
            for success in successList:          # 실패 단계 빼고 전체에서 성공할 확률
                result *= successPrs[success]/100
            for fail in failList:
                result *= (failPrs[fail]) / 100       # 해당 단계에서 실패할 확률
                if fail == 15:          # 15성에서는 실패해도 강화 등급 유지
                    result *= (successPrs[fail]/100)
                    # 실패하고 해당 단계에서 다시 성공할 확률
                else:
                    result *= (successPrs[fail-1]/100)*(successPrs[fail]/100)
                # 실패하고 이전 단계에서 성공하고 해당 단계에서 다시 성공할 확률

            result = result*100
            i_result += result          # i번 실패하고 성공할 확률
        final_result += i_result

    print(f"n={n} 일 때 : {float(format(final_result, '.20f'))}%")
