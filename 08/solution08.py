# Advent of Code
# 2022 Dec 8
import sys

# tree is a 5 tuple
# 0 1 2 3 4
# h N W E S

def aoc1():
	# read grid
	trees = []
	for line in sys.stdin:
		line = line.strip()
		tree_row = []
		trees.append(tree_row)
		for c in line:
			tree_row.append([int(c), None, None, None, None])
	row_count = len(trees)
	col_count = len(trees[0])

	# calc visible
	def visible(row, col):
		tree = trees[row][col]
		h = tree[0]
		if tree[1] == None:
			tree[1] = max_direction(row - 1, col, 1)
		if h > tree[1]:
			return True
		if tree[2] == None:
			tree[2] = max_direction(row, col - 1, 2)
		if h > tree[2]:
			return True
		if tree[3] == None:
			tree[3] = max_direction(row, col + 1, 3)
		if h > tree[3]:
			return True
		if tree[4] == None:
			tree[4] = max_direction(row + 1, col, 4)
		if h > tree[4]:
			return True
		return False
		
	def max_direction(row, col, dir):
		if dir == 1:
			if row < 0:
				return -1
			else:
				tree = trees[row][col]
				if tree[1] == None:
					tree[1] = max_direction(row - 1, col, 1)
				return max(tree[0], tree[1])
		if dir == 2:
			if col < 0:
				return -1
			else:
				tree = trees[row][col]
				if tree[2] == None:
					tree[2] = max_direction(row, col - 1, 2)
				return max(tree[0], tree[2])
		if dir == 3:
			if col >= col_count:
				return -1
			else:
				tree = trees[row][col]
				if tree[3] == None:
					tree[3] = max_direction(row, col + 1, 3)
				return max(tree[0], tree[3])
		if dir == 4:
			if row >= row_count:
				return -1
			else:
				tree = trees[row][col]
				if tree[4] == None:
					tree[4] = max_direction(row + 1, col, 4)
				return max(tree[0], tree[4])
	
	visible_tree_count = 0
	for tree_row in range(0, row_count):
		for tree_column in range(0, col_count):
			if(visible(tree_row, tree_column)):
				visible_tree_count += 1

	print(visible_tree_count)

	pass

def aoc2():
	# read grid
	trees = []
	for line in sys.stdin:
		line = line.strip()
		tree_row = []
		trees.append(tree_row)
		for c in line:
			tree_row.append([int(c), None, None, None, None])
	row_count = len(trees)
	col_count = len(trees[0])

	# calc visible
	def visible(row, col):
		tree = trees[row][col]
		h = tree[0]
		if tree[1] == None:
			tree[1] = max_direction(row - 1, col, 1, h)
		if tree[1] == 0:
			return 0
		if tree[2] == None:
			tree[2] = max_direction(row, col - 1, 2, h)
		if tree[2] == 0:
			return 0
		if tree[3] == None:
			tree[3] = max_direction(row, col + 1, 3, h)
		if tree[3] == 0:
			return 0
		if tree[4] == None:
			tree[4] = max_direction(row + 1, col, 4, h)
		if tree[4] == 0:
			return 0
		return tree[1] * tree[2] * tree[3] * tree[4]
		
	def max_direction(row, col, dir, h):
		if dir == 1:
			if row < 0:
				return 0
			else:
				tree = trees[row][col]
				if h > tree[0]:
					return 1 + max_direction(row - 1, col, 1, h)
				else:
					return 1
		if dir == 2:
			if col < 0:
				return 0
			else:
				tree = trees[row][col]
				if h > tree[0]:
					return 1 + max_direction(row, col - 1, 2, h)
				else:
					return 1
		if dir == 3:
			if col >= col_count:
				return 0
			else:
				tree = trees[row][col]
				if h > tree[0]:
					return 1 + max_direction(row, col + 1, 3, h)
				else:
					return 1
		if dir == 4:
			if row >= row_count:
				return 0
			else:
				tree = trees[row][col]
				if h > tree[0]:
					return 1 + max_direction(row + 1, col, 4, h)
				else:
					return 1
	
	max_score = 0
	for tree_row in range(0, row_count):
		for tree_column in range(0, col_count):
			temp_score = visible(tree_row, tree_column)
			if(temp_score > max_score):
				max_score = temp_score

	print(max_score)

	pass