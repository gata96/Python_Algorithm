def solution(bin1, bin2):
    int1, int2 = int(bin1,2), int(bin2,2) # bin(2진수)를 int로 변환
    # print(bin1, bin2) 10 11
    # print(int1,int2) 2 3
    # print(bin(int1+int2)) 0b101
    return bin(int1+int2)[2:]