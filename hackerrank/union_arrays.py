"""
You are given two arrays a[] and b[], return the Union of both the arrays in any order.

The Union of two arrays is a collection of all distinct elements present in either of the 
arrays. If an element appears more than once in one or both arrays, it should be included 
only once in the result.

Note: Elements of a[] and b[] are not necessarily distinct.
Note that, You can return the Union in any order but the driver code will print the result 
in sorted order only.

Examples:
Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
Output: [1, 2, 3]
Explanation: Union set of both the arrays will be 1, 2 and 3.


Input: a[] = [1, 2, 3], b[] = [4, 5, 6] 
Output: [1, 2, 3, 4, 5, 6] 
Explanation: Union set of both the arrays will be 1, 2, 3, 4, 5 and 6.


Input: a[] = [1, 2, 1, 1, 2], b[] = [2, 2, 1, 2, 1] 
Output: [1, 2]
Explanation: Union set of both the arrays will be 1 and 2.
"""




def union_set_array(a, b):
    """
    Combines two arrays
    
    :param a: the first input array
    :type a: List
    :param b: the second input array
    :type b: List
    :return: the combined list
    :rtype: List
    """

    # creating the new list
    newList = []

    seen = set()

    for x in a:
        if x not in seen:
            newList.append(x)
            seen.add(x)
    for j in b:
        if j not in seen:
            newList.append(j)
            seen.add(j)

    return newList

if __name__ == '__main__':
    a = [1, 2, 3] 
    b = [4, 5, 6]
    print(union_set_array(a=a, b=b))

