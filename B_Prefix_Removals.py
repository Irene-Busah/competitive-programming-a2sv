import sys

def find_longest_prefix(s):
    """
    Find the longest prefix of s that also appears elsewhere in s.
    Returns the length of this prefix (0 if none exists).
    """
    n = len(s)
    
    # Check prefixes from longest to shortest
    for length in range(n - 1, 0, -1):
        # s.find(pattern, start) searches for pattern starting from position 'start'
        # We start from position 1 to skip the prefix at position 0
        if s.find(s[:length], 1) != -1:
            return length
    
    return 0

def solve(s):
    """
    Recursively find and remove longest prefixes.
    Base case: when x=0 (no prefix found), return the string.
    Recursive case: remove the prefix and solve the rest.
    """
    x = find_longest_prefix(s)
    
    # Base case: no prefix found
    if x == 0:
        return s
    
    # Recursive case: remove prefix and continue
    return solve(s[x:])

def main():
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        s = sys.stdin.readline().rstrip('\n')
        result = solve(s)
        print(result)

if __name__ == "__main__":
    main()