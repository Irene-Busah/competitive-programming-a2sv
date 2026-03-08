"""
Alex and a group of friends communicate through a messaging app called ChatLoop.

The group contains 𝑛
 members (excluding Alex). Each member has a unique ID between 1
 and 𝑛
. Whenever someone opens the group chat, ChatLoop displays the list of members ordered by decreasing time of when they were last online (so the member who was online most recently appears first in the list). However, the exact timestamps are not shown.

Today Alex checked the group chat only twice: once at 9:00 and once at 22:00. Both times, Alex wrote down the list of members in the order shown by the app. Now Alex wants to know: what is the minimum number of members who must have gone online at least once between 9:00 and 22:00?

Alex is certain that no two members are ever online at the same time and that no members are online exactly at 9:00 or 22:00 when the chat is opened.

Input
Each test contains multiple test cases. The first line contains an integer 𝑡
 (1≤𝑡≤10000
) — the number of test cases. The descriptions of the 𝑡
 test cases follow.

The first line of each test case contains an integer 𝑛
 (1≤𝑛≤105
) — the number of members of the group excluding Alex.

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤𝑛
) — the list of IDs of the members, sorted by decreasing times of last seen online at 9:00.

The third line contains 𝑛
 integers 𝑏1,𝑏2,…,𝑏𝑛
 (1≤𝑏𝑖≤𝑛
) — the list of IDs of the members, sorted by decreasing times of last seen online at 22:00.

For all 1≤𝑖<𝑗≤𝑛
, it is guaranteed that 𝑎𝑖≠𝑎𝑗
 and 𝑏𝑖≠𝑏𝑗
.

It is also guaranteed that the sum of the values of 𝑛
 over all test cases does not exceed 105
.

Output
For each test case, print the minimum number of members that must have been online between 9:00 and 22:00.
"""



# importing necessary libraries
import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())






