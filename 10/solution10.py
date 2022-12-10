# Advent of Code
# 2022 Dec 10
import sys
import re

def aoc1():
	cycle = 0
	signal_sum = 0
	x = 1

	def cycle_calc():
		nonlocal signal_sum
		if (cycle - 20) % 40 == 0:
			signal_sum += x * cycle

	for line in sys.stdin:
		line = line.strip()
		if line == 'noop':
			cycle += 1
			#cycle start
			cycle_calc()
			#cycle end
		elif(match := re.match('addx ([0-9-]+)', line)):
			value = int(match.group(1))
			for i in range(0, 2):
				cycle += 1
				#cycle start
				cycle_calc()
				#cycle end
			x += value

	print(signal_sum)
	pass

def aoc2():
	cycle = 0
	x = 1

	def cycle_calc():
		if abs(((cycle - 1) % 40) - x) <= 1:
			print('#', end='')
		else:
			print('.', end='')
		if (cycle % 40) == 0:
			print('')

	for line in sys.stdin:
		line = line.strip()
		if line == 'noop':
			cycle += 1
			#cycle start
			cycle_calc()
			#cycle end
		elif(match := re.match('addx ([0-9-]+)', line)):
			value = int(match.group(1))
			for i in range(0, 2):
				cycle += 1
				#cycle start
				cycle_calc()
				#cycle end
			x += value

	pass