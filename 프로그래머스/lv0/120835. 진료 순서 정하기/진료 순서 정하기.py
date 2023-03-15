def solution(emergency): #3,76,24
    sorted_em = sorted(emergency, reverse = True) #76,24,3
    return [sorted_em.index(i)+1 for i in emergency]