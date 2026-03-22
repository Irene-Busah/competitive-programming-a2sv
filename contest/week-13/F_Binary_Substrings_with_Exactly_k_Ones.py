from collections import defaultdict
import sys


def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()

k = getInt()
s = getStr()

if k == 0:
    count = 0
    curr = 0
    for c in s:
        if c == '0':
            curr += 1
        else:
            count += curr * (curr + 1) // 2
            curr = 0
    count += curr * (curr + 1) // 2
    print(count)
    sys.exit()

freq = defaultdict(int)
freq[0] = 1

prefix = 0
count = 0

for c in s:
    if c == '1':
        prefix += 1

    count += freq[prefix - k]
    freq[prefix] += 1

print(count)