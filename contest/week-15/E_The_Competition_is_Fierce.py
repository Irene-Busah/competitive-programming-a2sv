"""
Ephrem the Professor is an organizer of a G7 Practice Contest event. There are 𝑛
 Groups in G7 Remote education numbered from 1
 to 𝑛
. Ephrem knows all competitive programmers in G7. There are 𝑛
 students: the 𝑖
-th student is enrolled at a Group 𝑢𝑖
 and has a programming skill 𝑠𝑖
.

Ephrem has to decide on the rules now. In particular, the number of members in the team.

Polycarp knows that if he chooses the size of the team to be some integer 𝑘
, each Group will send their 𝑘
 strongest (with the highest programming skill 𝑠
) students in the first team, the next 𝑘
 strongest students in the second team and so on. If there are fewer than 𝑘
 students left, then the team can't be formed. Note that there might be Groups that send zero teams.

The strength of the G7 is the total skill of the members of all present teams. If there are no teams present, then the strength is 0
.

Help Ephrem to find the strength of G7 for each choice of 𝑘
 from 1
 to 𝑛
.

Input
The first line contains a single integer 𝑡
 (1≤𝑡≤1000
) — the number of testcases.

The first line of each testcase contains a single integer 𝑛
 (1≤𝑛≤2⋅105
) — the number of Groups and the number of students.

The second line of each testcase contains 𝑛
 integers 𝑢1,𝑢2,…,𝑢𝑛
 (1≤𝑢𝑖≤𝑛
) — the Group the 𝑖
-th student is enrolled at.

The third line of each testcase contains 𝑛
 integers 𝑠1,𝑠2,…,𝑠𝑛
 (1≤𝑠𝑖≤109
) — the programming skill of the 𝑖
-th student.

The sum of 𝑛
 over all testcases doesn't exceed 2⋅105
.

Output
For each testcase print 𝑛
 integers: the strength of G7  — the total skill of the members of the present teams — for each choice of team size 𝑘
.
"""


from collections import defaultdict
import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfTestCases = getInt()


for _ in range(numOfTestCases):
    numOfStudents = getInt()

    u = list(map(int, input().split()))
    s = list(map(int, input().split()))

    groups = defaultdict(list)
    for i in range(numOfStudents):
        groups[u[i]].append(s[i])

    # sort and compute prefix sums
    prefix_sums = {}
    for g, skills in groups.items():
        skills.sort(reverse=True)
        ps = [0] * len(skills)
        ps[0] = skills[0]
        for i in range(1, len(skills)):
            ps[i] = ps[i-1] + skills[i]
        prefix_sums[g] = ps

    # answer array for k = 1..n
    ans = [0] * numOfStudents

    # for each group
    for ps in prefix_sums.values():
        m = len(ps)
        # contribution to each k
        for k in range(1, m+1):
            full_teams = m // k
            if full_teams > 0:
                ans[k-1] += ps[full_teams*k - 1]

    print(*ans)



