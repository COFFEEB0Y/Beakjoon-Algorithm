# ATM

"""
줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때
각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.
"""

import sys

N = int(sys.stdin.readline())

P = list(map(int, sys.stdin.readline().split()))

# 오름차순으로 정렬시키고 prefix_sum으로 더하기
P = sorted(P)
prefix_sum = []
s = 0
for i in range(len(P)):
    s += P[i]
    prefix_sum.append(s)

print(sum(prefix_sum))