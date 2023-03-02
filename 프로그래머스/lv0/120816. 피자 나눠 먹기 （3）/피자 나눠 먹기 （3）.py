def solution(slice, n):
    mok = n // slice
    if n % slice != 0:
        mok = mok + 1
        return mok
    else:
        return mok