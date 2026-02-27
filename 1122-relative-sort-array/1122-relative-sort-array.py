class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = {}
        res = []

        for i in range(len(arr1)):
            if arr1[i] not in hashmap:
                hashmap[arr1[i]] = 1
            else:
                hashmap[arr1[i]] += 1
        
        for i in arr2:
            while hashmap[i] > 0:
                res.append(i)
                hashmap[i] -= 1
        
        for key in sorted(hashmap.keys()):
            while hashmap[key] > 0:
                res.append(key)

                hashmap[key] -= 1
        
        return res