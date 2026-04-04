"""
So, Macaque has passed his first challenge (and is not acknowledging your help whatsoever). After all, it was only given to him so he could engage in his greatest pleasure — crunching on desiccated freezedried hamburgers and yelling 'trivial' at the screen. However, he has another, much more important task ahead of him, and he has once again enlisted you to help him.

You are given 7
 integers 𝑎1,𝑎2,…,𝑎7
.

You must negate 6
 out of the 7
 integers (that is, multiply them by −1
). Over all possible ways to negate 6
 out of the 7
 integers, find the maximum possible sum of 𝑎
.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤6767
). The description of the test cases follows.

The first and only line of each test case contains 7
 space-separated integers 𝑎1,𝑎2,…,𝑎7
 (−67≤𝑎𝑖≤67
).

Output
For each test case, output the maximum sum of 𝑎
 after negating 6
 out of the 7
 integers, on a new line.
"""


from utils.funcs import getInt, getIntList


numOfTestCases = getInt()

for _ in range(numOfTestCases):
    integers = getIntList()

    integers.sort()

    # integers = sorted(getIntList())
    result = -sum(integers[:6]) + integers[6]
    print(result)

