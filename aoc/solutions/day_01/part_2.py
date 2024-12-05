# coding: utf-8
lefts, rights = [], []

with open("inputs/day_01.txt") as f:
    for row in f.readlines():
        left, right = row.strip().split()
        lefts.append(int(left))
        rights.append(int(right))
lefts
rights
diffs = []
for left, right in zip(sorted(lefts), sorted(rights)):
    diffs.append(abs(left - right))
diffs
sum(diffs)
sims = []
for left in lefts:
    sims.append(left * rights.count(left))
    
print(sum(sims))
