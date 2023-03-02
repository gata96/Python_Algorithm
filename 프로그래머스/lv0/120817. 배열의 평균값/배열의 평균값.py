def solution(numbers):
    total = 0 
    for _ in numbers:
        total += _
    return(total / len(numbers))
# return 대신 print라고 하면 출력이 안된다.
