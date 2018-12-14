import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(n,scores, alice):
    resArr = []
    leaderboard = sorted(set(scores), reverse = True)
    l = len(leaderboard)
    for a in alice:
        while (l > 0) and (a >= leaderboard[l-1]):
            l -= 1
        resArr.append(l+1)
    return resArr

if __name__ == '__main__':
    
    result = climbingLeaderboard(7,[100, 100, 50, 40, 40, 20, 10],[5, 25,25, 50, 120])

    print(result)
