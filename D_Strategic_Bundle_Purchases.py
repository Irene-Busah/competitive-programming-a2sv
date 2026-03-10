"""
You want to purchase 𝑛
 items with prices 𝑎1,𝑎2,…,𝑎𝑛
. You can either:

buy item 𝑖
 individually, paying 𝑎𝑖
 coins, or
use a bundle coupon to include it as part of a grouped purchase.
You have 𝑘
 bundle coupons with values 𝑏1,𝑏2,…,𝑏𝑘
. A coupon of value 𝑥
 allows you to select exactly 𝑥
 items and pay only for the 𝑥−1
 most expensive ones, as such, you can consider that the cheapest item in the group is free. Each item can be included in at most one bundle group, even if it is not the free one. Also, any single coupon can be used at most one single time.

What is the minimum total cost required to purchase all 𝑛
 items?

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤104
). The description of the test cases follows.

The first line contains two integers 𝑛
 and 𝑘
 (1≤𝑛,𝑘≤2⋅105
) —the number of items and the number of available bundle coupons.

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤109
) — the prices of the items.

The third line contains 𝑘
 integers 𝑏1,𝑏2,…,𝑏𝑘
 (1≤𝑏𝑖≤𝑛
) — the values of the bundle coupons.

It is guaranteed that the sum of 𝑛
 across all test cases does not exceed 2⋅105
, and the sum of 𝑘
 across all test cases does not exceed 2⋅105
.

Output
Print 𝑡
 lines. The 𝑖
-th line should contain the answer for the 𝑖
-th test case — the minimum total cost required to purchase all items in that test case.
"""


# importing necessary libraries
import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))

"""
5 3
18 3 7 2 9
3 1 1

18 9 7 3 2

18 9 7
free = 7
3 2 = 12

18 9 7 3 2 = total cost - 18 - 9 - 2

18
9
2
"""



numOfTestCases = getInt()

for _ in range(numOfTestCases):
    # getting each test case data
    numOfItems, availableCoupons = getIntList()
    prices = getIntList()
    coupons = getIntList()

    # sorting the items and coupons
    prices.sort(reverse=True)
    coupons.sort()

    # getting the cost
    cost = sum(prices)

    index = 0

    for x in coupons:
        if index + x - 1 < numOfItems:
            free = prices[index + x - 1]
            cost = cost - free
            index += x
        
    print(cost)

