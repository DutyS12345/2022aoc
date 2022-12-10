# Advent of Code
# 2022 Dec 9
import sys
import re

def aoc1():
	tail_visited = {}
	h = [0, 0]
	t = [0, 0]

	def move_head(direction):
		if direction == 'R':
			h[0] += 1
		elif direction == 'U':
			h[1] += 1
		elif direction == 'L':
			h[0] -= 1
		elif direction == 'D':
			h[1] -= 1

	def move_tail():
		if(t[0] >= h[0] + 2):
			t[0] -= 1
			t[1] = h[1]
		elif(t[0] <= h[0] - 2):
			t[0] += 1
			t[1] = h[1]
		elif(t[1] >= h[1] + 2):
			t[1] -= 1
			t[0] = h[0]
		elif(t[1] <= h[1] - 2):
			t[1] += 1
			t[0] = h[0]
		tail_visited[str(t[0]) + ' ' + str(t[1])] = True

	for line in sys.stdin:
		if(match := re.match('(R|U|L|D) (\\d+)', line)):
			direction = match.group(1)
			distance = int(match.group(2))
			for i in range(0, distance):
				move_head(direction)
				move_tail()

	print(len(tail_visited))

	pass

def aoc2():
	tail_visited = {}
	knots = []
	knot_count = 10
	for i in range(0, knot_count):
		knots.append([0,0])

	def move_head(direction):
		h = knots[0]
		if direction == 'R':
			h[0] += 1
		elif direction == 'U':
			h[1] += 1
		elif direction == 'L':
			h[0] -= 1
		elif direction == 'D':
			h[1] -= 1

	def move_tail(k):
		h = knots[k - 1]
		t = knots[k]
		if(t[0] >= h[0] + 2):
			t[0] -= 1
			if(h[1] > t[1]):
				t[1] += 1
			elif(h[1] < t[1]):
				t[1] -= 1
		elif(t[0] <= h[0] - 2):
			t[0] += 1
			if(h[1] > t[1]):
				t[1] += 1
			elif(h[1] < t[1]):
				t[1] -= 1
		elif(t[1] >= h[1] + 2):
			t[1] -= 1
			if(h[0] > t[0]):
				t[0] += 1
			elif(h[0] < t[0]):
				t[0] -= 1
		elif(t[1] <= h[1] - 2):
			t[1] += 1
			if(h[0] > t[0]):
				t[0] += 1
			elif(h[0] < t[0]):
				t[0] -= 1
		if k == knot_count - 1:
			tail_visited[str(t[0]) + ' ' + str(t[1])] = True

	line_count = 0
	for line in sys.stdin:
		if(match := re.match('(R|U|L|D) (\\d+)', line)):
			direction = match.group(1)
			distance = int(match.group(2))
			for i in range(0, distance):
				move_head(direction)
				for k in range(1, knot_count):
					move_tail(k)
					
	print(len(tail_visited))

	pass