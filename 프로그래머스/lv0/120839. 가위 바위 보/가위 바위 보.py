def solution(rsp):
    result = {'2':'0','0':'5','5':'2'}
    return ''.join([result.get(i) for i in rsp])
        # dict[key]를 사용해서 value를 가져옴.
    