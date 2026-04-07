import sys
from math import gcd

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m, a, b = map(int, sys.stdin.readline().split())
        
        # Check if we can reach all rows and columns
        if gcd(a, n) != 1 or gcd(b, m) != 1:
            print("NO")
            continue
        
        # Check additional constraint:
        # - Either gcd(n, m) = 1
        # - Or n = m and gcd(a, b) = 1
        g_nm = gcd(n, m)
        g_ab = gcd(a, b)
        
        if g_nm == 1 or (n == m and g_ab == 1):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()