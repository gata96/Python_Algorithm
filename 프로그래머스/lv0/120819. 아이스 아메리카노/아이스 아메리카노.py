def solution(money):
    cup = money // 5500
    charge = money - cup * 5500
    result = []
    result.append(cup)
    result.append(charge)
    return result