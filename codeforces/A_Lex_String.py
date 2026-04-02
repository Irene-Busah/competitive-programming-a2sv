"""
Kuznecov likes art, poetry, and music. And strings consisting of lowercase English letters.

Recently, Kuznecov has found two strings, 𝑎
 and 𝑏
, of lengths 𝑛
 and 𝑚
 respectively. They consist of lowercase English letters and no character is contained in both strings.

Let another string 𝑐
 be initially empty. Kuznecov can do the following two types of operations:

Choose any character from the string 𝑎
, remove it from 𝑎
, and add it to the end of 𝑐
.
Choose any character from the string 𝑏
, remove it from 𝑏
, and add it to the end of 𝑐
.


But, he can not do more than 𝑘
 operations of the same type in a row. He must perform operations until either 𝑎
 or 𝑏
 becomes empty. What is the lexicographically smallest possible value of 𝑐
 after he finishes?

A string 𝑥
 is lexicographically smaller than a string 𝑦
 if and only if one of the following holds:

𝑥
 is a prefix of 𝑦
, but 𝑥≠𝑦
;
in the first position where 𝑥
 and 𝑦
 differ, the string 𝑥
 has a letter that appears earlier in the alphabet than the corresponding letter in 𝑦
.
Input
There are several test cases in the input data. The first line contains a single integer 𝑡
 (1≤𝑡≤100
) — the number of test cases. This is followed by the test cases description.

The first line of each test case contains three integers 𝑛
, 𝑚
, and 𝑘
 (1≤𝑛,𝑚,𝑘≤100
) — parameters from the statement.

The second line of each test case contains the string 𝑎
 of length 𝑛
.

The third line of each test case contains the string 𝑏
 of length 𝑚
.

The strings contain only lowercase English letters. It is guaranteed that no symbol appears in 𝑎
 and 𝑏
 simultaneously.

Output
In each test case, output a single string 𝑐
 — the answer to the problem.
"""


from utils.funcs import getInt, getIntList, getStr


numOfTestCases = getInt()

for _ in range(numOfTestCases):
    n, m, k = getIntList()

    a = sorted(getStr())
    b = sorted(getStr())

    c = []

    count_a = 0
    count_b = 0

    while a and b:
        if count_a == k:
            c.append(b[0])
            b.pop(0)
            count_b += 1
            count_a = 0
        elif count_b == k:
            c.append(a[0])
            a.pop(0)
            count_a += 1
            count_b = 0
        else:
            if a[0] < b[0]:
                c.append(a[0])
                a.pop(0)
                count_a += 1
                count_b = 0
            else:
                c.append(b[0])
                b.pop(0)
                count_b += 1
                count_a = 0
    c = "".join(c)
    print(c)




