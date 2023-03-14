import numpy as np
def solution(num_list, n):
    return (np.array(num_list).reshape((len(num_list) // n ,n))).tolist()

    # num_list # [1, 2, 3, 4, 5, 6, 7, 8]
    # np.array(num_list) # [1 2 3 4 5 6 7 8]
    # reshape((len(num_list) // n ,n))
    # [[1 2]
    # [3 4]
    # [5 6]
    # [7 8]]
    # tolist() # [[1, 2], [3, 4], [5, 6], [7, 8]]
    
   