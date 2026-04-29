"""
A space agency is preparing missions to explore distant planets. There are 𝑁 astronauts 
available, and each astronaut has a skill level 𝑃𝑖.

These astronauts will be trained and led by Commander Mikias Goitom. He will form zero or more 
mission teams from the astronauts, where each astronaut may join at most one team. Each team 
can consist of any number of astronauts.

Each team will attempt a mission with difficulty level 𝐷. A team successfully completes a mission 
if the total effective skill of the team is strictly greater than 𝐷.

Commander Mikias Goitom has a special ability: before a mission begins, he can synchronize the 
team so that all astronauts in a team have their skill adjusted to be equal to the maximum skill 
among the members of that team.

Determine the maximum number of successful missions that can be achieved under Commander Mikias Goitom.

Input
The first line contains two integers 𝑁 and 𝐷 (1≤𝑁≤105, 1≤𝐷≤109) — the number of astronauts and 
the difficulty of the mission.

The second line contains 𝑁 integers 𝑃1,𝑃2,…,𝑃𝑁 (1≤𝑃𝑖≤109) — the skill levels of the astronauts.

Output
Output a single integer representing the maximum number of successful missions.
"""


import math
import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfAstronauts, difficultyOfMission = getIntList()
skillsLevel = getIntList()

skillsLevel.sort(reverse=True)

teams = 0
i = 0
remaining_tail = numOfAstronauts - 1  # index of weakest available astronaut

while i <= remaining_tail:
    leader = skillsLevel[i]
    needed = math.ceil((difficultyOfMission + 1) / leader)  # minimum team size
    
    fillers = needed - 1  # how many extra members needed besides leader
    
    if remaining_tail - i >= fillers:
        teams += 1
        remaining_tail -= fillers  # consume fillers from the weak end
    
    i += 1  # move to next potential leader

print(teams)



