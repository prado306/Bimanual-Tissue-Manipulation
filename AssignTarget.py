import numpy as np

def findRelativeCoord(arr):

    result = [0] * len(arr)
    for i,val in enumerate(arr):
        if i%2==0:
            result[i] = round(arr[i]/8.0 * 0.1 + 0.5, 2)

        else:
            result[i] = round(arr[i]/6.0 * 0.1 + 0.5, 2)
    
    # x = (numx/8.0 * 0.1 + 0.5)
    # y = (numy/6.0 * 0.1 + 0.5)

    return result