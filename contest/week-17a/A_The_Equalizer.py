"""
To settle a long-time feud, Shaunak and Yash decided to play a game on an array 𝑎
 of 𝑛
 integers, with Shaunak going first. The players take turns, and the last player to make a move wins. On a player's turn, he chooses some 𝑎𝑖>0
 and decrements it by 1
.

To make things interesting, Shaunak is allowed to use a special move at most once during the game. This move replaces his normal turn. When used, all elements 𝑎𝑖
 (1≤𝑖≤𝑛
) are set to a special value 𝑘
 that is given initially.

Assuming that both players play optimally, determine if Shaunak can always win.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤500
). The description of the test cases follows.

The first line of each test case contains two integers 𝑛
 and 𝑘
 (1≤𝑛≤100
, 1≤𝑘≤500
), denoting the size of the array and the special value.

The second line contains 𝑛
 integers 𝑎1,𝑎2,…,𝑎𝑛
 (1≤𝑎𝑖≤103
).

Output
For each test case, print "YES" if Shaunak can always win, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
"""


import sys
from functools import reduce
from operator import xor
 
 
def can_shaunak_win(n, k, a):
    """
    Determine if Shaunak can always win with optimal play.
    
    Returns: True if Shaunak can win, False otherwise
    """
    
    # Calculate XOR of original array
    xor_original = reduce(xor, a, 0)
    
    # In Nim: XOR ≠ 0 means current player (Shaunak) can win
    if xor_original != 0:
        return True
    
    # If original position is losing, check if special move can help
    # After special move, all elements are k, so we have n copies of k
    # XOR of n k's is: k if n is odd, 0 if n is even
    xor_special = 0
    for _ in range(n):
        xor_special ^= k
    
    # After using special move, it's Yash's turn with XOR = xor_special
    # Shaunak wins if Yash is in a losing position, i.e., XOR = 0
    if xor_special == 0:
        return True
    
    # Neither strategy works
    return False
 
 
def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        if can_shaunak_win(n, k, a):
            print("YES")
        else:
            print("NO")
 
 
if __name__ == "__main__":
    main()

