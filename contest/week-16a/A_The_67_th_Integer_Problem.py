"""
Welcome to the New World, O Esteemed Earthly Visitor. You've been summoned by Macaque, a primate with four legs, a god complex and a terminal addiction to the word "trivial". You are Undertaking a Journey of Great Importance. Such Incredible Importance. No Journey Will EVER be as IMPORTANT as this one (and nothing this narrator says will sound so distinctly... orange again). You are implored to cooperate with Macaque, for his wrath (and joblessness) are unending. There is no room for error or incompetence. Lousiness shall be met with the full force of the law.

Macaque is given an integer 𝑥
. Your task is to choose an integer 𝑦
 such that the value of min(𝑥,𝑦)
∗
 is maximized.

If there are multiple valid 𝑦
, you may output any of them.

∗
min(𝑥,𝑦)
 is defined as the minimum of integers 𝑥
 and 𝑦
.

Input
Each test contains multiple test cases. The first line contains the number of test cases 𝑡
 (1≤𝑡≤6767
). The description of the test cases follows.

The only line of each test case contains a single integer 𝑥
 (−67≤𝑥≤67
).

Output
For each test case, output one integer 𝑦
 (−67≤𝑦≤67
) such that min(𝑥,𝑦)
 is maximized.
"""


from utils.funcs import getInt

numOftestCases = getInt()

for _ in range(numOftestCases):
    x = getInt()

    y = x 
    print(y)
