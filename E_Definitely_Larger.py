def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        d = list(map(int, input().split()))
        
        # Convert p to 0-indexed
        p = [x - 1 for x in p]
        
        # Feasibility check: for each position i, count how many j > i have p[j] > p[i]
        # If d[i] exceeds this count, no valid solution exists
        possible = True
        for i in range(n):
            candidates_count = sum(1 for j in range(i + 1, n) if p[j] > p[i])
            if d[i] > candidates_count:
                possible = False
                break
        
        if not possible:
            print(-1)
            continue
        
        # Construct q using right-to-left processing with backtracking
        # Process from position n-1 down to 0 since we need to know future q values
        q = [0] * n
        available = list(range(1, n + 1))
        
        def construct(pos):
            """Build q from position pos down to 0"""
            if pos < 0:
                return True
            
            # Find candidate positions: j > pos where p[j] > p[pos]
            candidates = [j for j in range(pos + 1, n) if p[j] > p[pos]]
            candidate_values = [q[j] for j in candidates]
            
            # Find all valid values for position pos:
            # A value is valid if exactly d[pos] of the candidate values are greater than it
            valid_values = []
            for val in available:
                count_greater = sum(1 for cv in candidate_values if cv > val)
                if count_greater == d[pos]:
                    valid_values.append(val)
            
            # Try each valid value with backtracking
            for val in sorted(valid_values):
                q[pos] = val
                available.remove(val)
                
                if construct(pos - 1):
                    return True
                
                available.append(val)
                q[pos] = 0
            
            return False
        
        if construct(n - 1):
            print(' '.join(map(str, q)))
        else:
            print(-1)

solve()
