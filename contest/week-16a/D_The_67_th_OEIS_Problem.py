"""
Macaque, being a terrible problemsetter, decided to search for funny sequences on the OEIS∗
 one day, so he could gain inspiration for his doomed problemsetting job for the Pan-Mammalian Olympiad in Informatics (PMOI). To his delight, he found one, and thought it would be funny to make you, his loyal tester, solve it:

Construct a sequence 𝑎
 containing 𝑛
 integers such that gcd(𝑎𝑖,𝑎𝑖+1)
 †
 is distinct over all 1≤𝑖≤𝑛−1
. It is guaranteed that at least one sequence 𝑎
 exists.

∗
Online Encyclopedia of Integer Sequences, the favourite website of math nerds, overly astute testers, and insufficiently rigorous coordinators.

†
gcd(𝑥,𝑦)
 refers to the greatest common divisor of integers 𝑥
 and 𝑦
.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤100
). The description of the test cases follows.

The following 𝑡
 lines contain one integer 𝑛
 (2≤𝑛≤104
) — the desired length of the sequence.

It is guaranteed the sum of 𝑛
 over all test cases does not exceed 104
.

Output
For each query, output your answer — a sequence 𝑎
 of 𝑛
 space-separated integers (1≤𝑎𝑖≤1018
).
"""



import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())


# def sieve(limit):
#     """Generate all primes up to limit using Sieve of Eratosthenes"""
#     is_prime = [True] * (limit + 1)
#     is_prime[0] = is_prime[1] = False
    
#     for i in range(2, int(limit**0.5) + 1):
#         if is_prime[i]:
#             for j in range(i*i, limit + 1, i):
#                 is_prime[j] = False
    
#     return [i for i in range(2, limit + 1) if is_prime[i]]

# # Pre-compute primes (need at most 10000 primes for n ≤ 10^4)
# primes = sieve(130000) 

# numOfTestCase = getInt()

# for _ in range(numOfTestCase):
#     n = getInt()
#     res = []
#     product = 1
    
#     for i in range(n):
#         product *= primes[i]
#         res.append(product)
    
#     print(*res)


numOfTestCases = getInt()

for _ in range(numOfTestCases):
    n = getInt()
    
    # Construct decreasing sequence starting from 2*n
    res = [2*n - i for i in range(n)]
    
    print(*res)

