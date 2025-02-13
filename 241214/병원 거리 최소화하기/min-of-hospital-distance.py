# 좌표 차가 거리 N*N 격자 병원은 m개만 남길 것. 
# 병원에 대한 사람들의 거리 총 합이 최소가 되도록 할 것
import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
hospital, person = [], []
for y in range(n):
    tmp = list(map(int, input().split()))
    for x in range(n):
        if tmp[x] == 1 : person.append([x,y])
        elif tmp[x] == 2 : hospital.append([x,y])

answer = float('inf')
for hospitals in combinations(hospital, m):
    total_dist = 0
    for p in person:
        min_dist = float('inf')
        for h in hospitals:
            tmp = abs(h[0]-p[0]) + abs(h[1]-p[1])
            min_dist = min(min_dist, tmp)
        total_dist += min_dist
    answer = min(answer, total_dist)

print(answer)