# Advent of Code
# 2022 Dec 2
import sys

# A B C
# X Y Z
# R P S
# 1 2 3

def aoc1():
	rps = {
		'A' : 1,
		'B' : 2,
		'C' : 3,
		'X' : 1,
		'Y' : 2,
		'Z' : 3,
	}
	score = 0
	for line in sys.stdin:
		enemy = rps[line[0]]
		strat = rps[line[2]]
		if enemy == strat:
			score += 3
		elif enemy == strat - 1 or (strat == 1 and enemy == 3):
			score += 6
		score += strat
	print(score)

def aoc2():
	rps = {
		'A' : 1,
		'B' : 2,
		'C' : 3,
		'X' : -1,
		'Y' : 0,
		'Z' : 1,
	}
	score = 0
	for line in sys.stdin:
		enemy = rps[line[0]]
		strat = rps[line[2]]
		pts = enemy + strat
		if pts < 1:
			pts = 3
		if pts > 3:
			pts = 1
		pts += (strat + 1) * 3
		score += pts
	print(score)

	pass