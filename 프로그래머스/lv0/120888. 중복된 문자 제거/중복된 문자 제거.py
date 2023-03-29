def solution(my_string):
    answer = ''
    for _ in my_string:
        if _ in answer:
            pass
        else:
            answer += _
    return answer