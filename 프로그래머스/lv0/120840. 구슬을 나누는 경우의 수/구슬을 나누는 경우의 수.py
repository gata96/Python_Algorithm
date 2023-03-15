def facto(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
        
def solution(balls, share):
    n = balls
    m = share
    return facto(n)/(facto(n-m) * facto(m))


                        