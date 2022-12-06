# Advent of Code
# 2022 Dec 5
import sys
import re

lines = []
def aoc1():
	# setup stacks
	line_idx = 0
	for line in sys.stdin:
		lines.append(line)
		if line.strip() == '':
			gap = line_idx
		line_idx += 1
	stacks = [[] for x in range(0, (len(lines[0])) // 4)]
	for i in range(gap - 2, -1, -1):
		for s in range(len(stacks)):
			c = lines[i][s * 4 + 1]
			if c != ' ':
				stacks[s].append(c)
	print(stacks)
	# execute instructions
	for line in lines[gap + 1:]:
		match = re.match('move (\\d+) from (\\d+) to (\\d+)', line)
		if match:
			stack_1 = int(match.group(2)) - 1
			stack_2 = int(match.group(3)) - 1
			count = min(int(match.group(1)), len(stacks[stack_1]))
		for x in range(0, count):
			stacks[stack_2].append(stacks[stack_1].pop())
	total = ''
	for s in stacks:
		total += s[-1]
	print(total)
	# another way is dependency tree traversal
	pass

def aoc2():
	# setup stacks
	line_idx = 0
	for line in sys.stdin:
		lines.append(line)
		if line.strip() == '':
			gap = line_idx
		line_idx += 1
	stacks = [[] for x in range(0, (len(lines[0])) // 4)]
	for i in range(gap - 2, -1, -1):
		for s in range(len(stacks)):
			c = lines[i][s * 4 + 1]
			if c != ' ':
				stacks[s].append(c)
	print(stacks)
	# execute instructions
	temp_stack = []
	for line in lines[gap + 1:]:
		match = re.match('move (\\d+) from (\\d+) to (\\d+)', line)
		if match:
			stack_1 = int(match.group(2)) - 1
			stack_2 = int(match.group(3)) - 1
			count = min(int(match.group(1)), len(stacks[stack_1]))
		for x in range(0, count):
			temp_stack.append(stacks[stack_1].pop())
		for x in range(0, count):
			stacks[stack_2].append(temp_stack.pop())
	total = ''
	for s in stacks:
		total += s[-1]
	print(total)
	# another way is dependency tree traversal
	pass