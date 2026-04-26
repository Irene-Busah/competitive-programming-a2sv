"""
There is a country with 𝑛
 citizens. The 𝑖
-th of them initially has 𝑎𝑖
 money. The government strictly controls the wealth of its citizens. Whenever a citizen makes a purchase or earns some money, they must send a receipt to the social services mentioning the amount of money they currently have.

Sometimes the government makes payouts to the poor: all citizens who have strictly less money than 𝑥
 are paid accordingly so that after the payout they have exactly 𝑥
 money. In this case the citizens don't send a receipt.

You know the initial wealth of every citizen and the log of all events: receipts and payouts. Restore the amount of money each citizen has after all events.

Input
The first line contains a single integer 𝑛
 (1≤𝑛≤2⋅105
) — the numer of citizens.

The next line contains 𝑛
 integers 𝑎1
, 𝑎2
, ..., 𝑎𝑛
 (0≤𝑎𝑖≤109
) — the initial balances of citizens.

The next line contains a single integer 𝑞
 (1≤𝑞≤2⋅105
) — the number of events.

Each of the next 𝑞
 lines contains a single event. The events are given in chronological order.

Each event is described as either 1 p x (1≤𝑝≤𝑛
, 0≤𝑥≤109
), or 2 x (0≤𝑥≤109
). In the first case we have a receipt that the balance of the 𝑝
-th person becomes equal to 𝑥
. In the second case we have a payoff with parameter 𝑥
.

Output
Print 𝑛
 integers — the balances of all citizens after all events.
"""


import sys


# defining useful function for input data collection
def getInt(): return int(sys.stdin.readline().strip())
def getStr(): return sys.stdin.readline().strip()
def getIntSeq(): return map(int, sys.stdin.readline().strip().split())
def getStrSeq(): return sys.stdin.readline().strip().split()
def getIntList(): return list(map(int, sys.stdin.readline().strip().split()))
def getStrList(): return list(sys.stdin.readline().strip().split())


numOfCitizens = getInt()

initialBalances = getIntList()

numOfEvents = getInt()

for _ in range(numOfEvents):
    pass

