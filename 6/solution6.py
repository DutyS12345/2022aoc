# Advent of Code
# 2022 Dec 6
import sys

def aoc1():
	for line in sys.stdin:
		buffer_max_len = 4
		buffer = []
		for i in range(len(line)):
			c = line[i]
			buffer.append(c)
			if len(buffer) > buffer_max_len:
				buffer.pop(0)
			if len(buffer) == buffer_max_len \
			and len(set(buffer)) == buffer_max_len:
					print(i + 1)
					break

def aoc2():
	for line in sys.stdin:
		buffer_max_len = 14
		buffer = []
		for i in range(len(line)):
			c = line[i]
			buffer.append(c)
			if len(buffer) > buffer_max_len:
				buffer.pop(0)
			if len(buffer) == buffer_max_len \
			and len(set(buffer)) == buffer_max_len:
					print(i + 1)
					break
