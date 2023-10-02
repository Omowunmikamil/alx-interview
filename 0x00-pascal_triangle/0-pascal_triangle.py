#!/usr/bin/python3
""" pascal triangle
"""


def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []
    
    pascal = []
    
    for i in range(n):
        # first element
        my_List = [1]
        if i == 0:
            pascal.append(my_List)
            continue
        
        k = i - 1
        for j in range(len(pascal[k])):
            if j + 1 == len(pascal[k]):
                # last element
                my_List.append(1)
                break
            # Add two previous values to get current next value
            nextVal = pascal[k][j] + pascal[k][j + 1]
            my_List.append(nextVal)
        pascal.append(my_List)
        
    return pascal