def countingSort(arr):
    # Write your code here
    
    res = []
    
    counter = Counter(arr)
    
    arr.sort()
    
    for i in range(100):
        if i in counter.keys():
            val = counter[i]
            res.append(val)
        else:
            res.append(0)
        
    return res