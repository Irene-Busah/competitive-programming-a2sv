def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        p = int(input()) - 1  # Convert to 0-indexed
        
        x = a[p]
        
        # Determine which positions need to be flipped
        need_flip = [1 if a[i] != x else 0 for i in range(n)]
        
        # Count contiguous segments of 1s on the left side [0, p-1]
        left_segments = 0
        in_segment = False
        for i in range(p):
            if need_flip[i] == 1:
                if not in_segment:
                    left_segments += 1
                    in_segment = True
            else:
                in_segment = False
        
        # Count contiguous segments of 1s on the right side [p+1, n-1]
        right_segments = 0
        in_segment = False
        for i in range(p + 1, n):
            if need_flip[i] == 1:
                if not in_segment:
                    right_segments += 1
                    in_segment = True
            else:
                in_segment = False
        
        # Apply the formula
        total_segments = left_segments + right_segments
        if total_segments <= 2:
            answer = total_segments
        else:
            answer = max(left_segments, right_segments) * 2
        
        print(answer)
 
if __name__ == "__main__":
    solve()