"""
Arseniy came up with another business plan — to sell juice boxes from a vending machine! For this, he purchased a machine with 𝑛
 shelves, as well as 𝑘
 juice boxes, where the 𝑖
-th juice box is characterized by the brand index 𝑏𝑖
 and the cost 𝑐𝑖
.

You can place any number of juice box on each shelf, but all juice boxes on the same shelf must be of the same brand.

Arseniy knows that all the juice boxes he puts on the shelves of the machine will be sold. Therefore, he asked you to calculate the maximum amount he can earn.

Input
The first line contains one integer 𝑡
 (1≤𝑡≤104
) — the number of test cases.

The first line of each test case contains two integers 𝑛
 and 𝑘
 (1≤𝑛,𝑘≤2⋅105
), where 𝑛
 is the number of shelves in the machine, and 𝑘
 is the number of juice boxes available to Arseniy.

The next 𝑘
 lines contain two integers 𝑏𝑖
 and 𝑐𝑖
 (1≤𝑏𝑖≤𝑘,1≤𝑐𝑖≤1000
) — the brand and cost of the 𝑖
-th juice box.

It is also guaranteed that the sum of 𝑛
 across all test cases does not exceed 2⋅105
 and that the sum of 𝑘
 across all test cases also does not exceed 2⋅105
.

Output
For each test case, output one integer — the maximum amount that Arseniy can earn.
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfTesCases = getInt()

for _ in range(numOfTesCases):
    n, k = getIntList()

    brandSum = [0]*(k+1)


    for i in range(k):
        brand, cost = getIntList()
        brandSum[brand] += cost

        for i in range(k):
            brandSum[brand] 
        
        
    
    brandSum.sort(reverse=True)

    ans = sum(brandSum[:n])
    print(ans)
    # brandTotalCost.sort()

