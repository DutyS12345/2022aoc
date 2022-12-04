# Advent of Code
# 2022 Dec 3
import sys

# ord('a') == 97
# ord('A') == 65

def priority(x):
	char = ord(x)
	if char > 96:
		return char - 96
	return char - 38

def aoc1():
	total = 0
	for line in sys.stdin:
		halfway = len(line) >> 1
		left = set(line[0:halfway])
		for i in range(halfway, len(line)):
			if line[i] in left:
				total += priority(line[i])
				break
	print(total)

def aoc2():
	elf = 0
	total = 0
	for line in sys.stdin:
		line = line.strip()
		case = elf % 3
		if case == 0:
			common = set(line)
		elif case == 1:
			common = {x for x in line if x in common}
		elif case == 2:
			for c in line:
				if c in common:
					total += priority(c)
					break
		elf += aoc1
	print(total)
	