# Advent of Code
# 2022 Dec 12
import sys

def aoc1():
	grid = []
	i = 0
	for line in sys.stdin:
		line = line.strip()
		row = []
		grid.append(row)
		for j in range(len(line)):
			c = line[j]
			if(c == 'S'):
				s_coords = [i, j]
				row.append([1, True])
			elif(c == 'E'):
				e_coords = [i, j]
				row.append([26, False])
			else:
				row.append([ord(c) - 96, False])
		i += 1
	grid_width = len(grid)
	grid_height = len(grid[0])
	queue = [s_coords.copy()]
	def val(coords):
		return grid[coords[0]][coords[1]][0]

	def visit(coords):
		grid[coords[0]][coords[1]][1] = True

	def visited(coords):
		return grid[coords[0]][coords[1]][1]

	steps = -1
	found = False	
	while not found:
		next_queue = []
		for pos in queue:
			if (pos[0] == e_coords[0] and pos[1] == e_coords[1]):
				found = True
				break
			pos_value = val(pos)
			if pos[0] - 1 >= 0:
				next_pos = [pos[0] - 1, pos[1]]
				if pos_value + 1 >= val(next_pos) and not visited(next_pos):
					visit(next_pos)
					next_queue.append(next_pos)
			if pos[1] - 1 >= 0:
				next_pos = [pos[0], pos[1] - 1]
				if pos_value + 1 >= val(next_pos) and not visited(next_pos):
					visit(next_pos)
					next_queue.append(next_pos)
			if pos[0] + 1 < grid_width:
				next_pos = [pos[0] + 1, pos[1]]
				if pos_value + 1 >= val(next_pos) and not visited(next_pos):
					visit(next_pos)
					next_queue.append(next_pos)
			if pos[1] + 1 < grid_height:
				next_pos = [pos[0], pos[1] + 1]
				if pos_value + 1 >= val(next_pos) and not visited(next_pos):
					visit(next_pos)
					next_queue.append(next_pos)
		queue = next_queue 
		steps += 1
		if steps > grid_height * grid_height:
			print('error')
			break

	print(grid)
	print(steps)

	pass

def aoc2():
	grid = []
	i = 0
	for line in sys.stdin:
		line = line.strip()
		row = []
		grid.append(row)
		for j in range(len(line)):
			c = line[j]
			if(c == 'S'):
				s_coords = [i, j]
				row.append([1, False])
			elif(c == 'E'):
				e_coords = [i, j]
				row.append([26, True])
			else:
				row.append([ord(c) - 96, False])
		i += 1
	grid_width = len(grid)
	grid_height = len(grid[0])
	queue = [e_coords.copy()]
	def val(coords):
		return grid[coords[0]][coords[1]][0]

	def visit(coords):
		grid[coords[0]][coords[1]][1] = True

	def visited(coords):
		return grid[coords[0]][coords[1]][1]

	steps = -1
	found = False	
	while not found:
		next_queue = []
		for pos in queue:
			pos_value = val(pos)
			if (pos_value == 1):
				found = True
				break
			if pos[0] - 1 >= 0:
				next_pos = [pos[0] - 1, pos[1]]
				if pos_value - 1 <= val(next_pos) and not visited(next_pos):
					visit(next_pos)
					next_queue.append(next_pos)
			if pos[1] - 1 >= 0:
				next_pos = [pos[0], pos[1] - 1]
				if pos_value - 1 <= val(next_pos) and not visited(next_pos):
					visit(next_pos)
					next_queue.append(next_pos)
			if pos[0] + 1 < grid_width:
				next_pos = [pos[0] + 1, pos[1]]
				if pos_value - 1 <= val(next_pos) and not visited(next_pos):
					visit(next_pos)
					next_queue.append(next_pos)
			if pos[1] + 1 < grid_height:
				next_pos = [pos[0], pos[1] + 1]
				if pos_value - 1 <= val(next_pos) and not visited(next_pos):
					visit(next_pos)
					next_queue.append(next_pos)
		queue = next_queue 
		steps += 1
		if steps > grid_height * grid_height:
			print('error')
			break

	print(grid)
	print(steps)

	pass