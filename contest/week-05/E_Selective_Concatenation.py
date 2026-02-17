"""
In the A2SV remote classroom, students are divided into exactly k study groups. However, 
only the even-numbered groups submit their work for evaluation. The submissions are merged 
in order, and the instructor checks how well they match the expected sequence starting from 1.

You are given an array a of length n and an even integer k (2≤k≤n). You need to split the array a
into exactly k non-empty subarrays†
 such that each element of the array 𝑎
 belongs to exactly one subarray.

Next, all subarrays with even indices (second, fourth, …
, 𝑘
-th) are concatenated into a single array 𝑏
. After that, 0
 is added to the end of the array 𝑏
.

The cost of the array 𝑏
 is defined as the minimum index 𝑖
 such that 𝑏𝑖≠𝑖
. For example, the cost of the array 𝑏=[1,2,4,5,0]
 is 3
, since 𝑏1=1
, 𝑏2=2
, and 𝑏3≠3
. Determine the minimum cost of the array 𝑏
 that can be obtained with an optimal partitioning of the array 𝑎
 into subarrays.

†
An array 𝑥
 is a subarray of an array 𝑦
 if 𝑥
 can be obtained from 𝑦
 by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

Input
Each test consists of multiple test cases. The first line contains a single integer 𝑡
 (1≤𝑡≤104
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers 𝑛
 and 𝑘
 (2≤𝑘≤𝑛≤2⋅105
, 𝑘
 is even) — the length of the array 𝑎
 and the number of subarrays.

The second line of each test case contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤109
) — the elements of the array 𝑎
.

It is guaranteed that the sum of 𝑛
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output a single integer — the minimum cost of the array 𝑏
 that can be obtained.
"""