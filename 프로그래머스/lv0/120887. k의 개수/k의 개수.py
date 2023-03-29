def solution(i, j, k):
    answer = 0
    # i~j까지 숫자 추출
    for num in range(i, j+1):
        # num에서 k가 몇번 등장하는지 count
        while num:
            if num % 10 == k:
                answer += 1
            num //= 10 # num은 10으로 매번 나눠준다.
                
    return answer