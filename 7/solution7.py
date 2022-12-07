# Advent of Code
# 2022 Dec 7
import sys
import re

class TreeNode:
	def __init__(self, parent):
		self.subdirs = {}
		self.files = []
		self.size = 0
		self.parent = parent

def aoc1():
	# parse input tree
	root = TreeNode(None)
	cur = root
	for line in sys.stdin:
		line = line.strip()
		cd = re.match('\\$ cd (.*)', line)
		if cd:
			dirname = cd.group(1)
			if dirname == '/':
				cur = root
			elif dirname == '..':
				cur = cur.parent
				if cur == None:
					cur = root
			else:
				cur = cur.subdirs[dirname]
			continue
		if line == '$ ls':
			continue
		dircontents = re.match('([a-zA-Z0-9]+) ([a-zA-Z.]+)', line)
		if dircontents:
			if dircontents.group(1) == 'dir':
				cur.subdirs[dircontents.group(2)] = TreeNode(cur)
			else:
				cur.files.append((int(dircontents.group(1)), dircontents.group(2)))
		else:
			print('Error lmao')
	# traverse to calc sizes
	total = 0
	def calc_size(node):
		nonlocal total
		for dirname in node.subdirs:
			node.size += calc_size(node.subdirs[dirname])
		for file in node.files:
			node.size += file[0]
		if node.size <= 100_000:
			total += node.size
		return node.size
	calc_size(root)
	print(total)

def aoc2():
	# parse input tree
	root = TreeNode(None)
	cur = root
	for line in sys.stdin:
		line = line.strip()
		cd = re.match('\\$ cd (.*)', line)
		if cd:
			dirname = cd.group(1)
			if dirname == '/':
				cur = root
			elif dirname == '..':
				cur = cur.parent
				if cur == None:
					cur = root
			else:
				cur = cur.subdirs[dirname]
			continue
		if line == '$ ls':
			continue
		dircontents = re.match('([a-zA-Z0-9]+) ([a-zA-Z.]+)', line)
		if dircontents:
			if dircontents.group(1) == 'dir':
				cur.subdirs[dircontents.group(2)] = TreeNode(cur)
			else:
				cur.files.append((int(dircontents.group(1)), dircontents.group(2)))
		else:
			print('Error lmao')
	# traverse to calc sizes
	def calc_size(node):
		for dirname in node.subdirs:
			node.size += calc_size(node.subdirs[dirname])
		for file in node.files:
			node.size += file[0]
		return node.size
	calc_size(root)

	# traverse to find min size above threshold
	threshold = root.size - (70_000_000 - 30_000_000)
	min_val = root.size
	def find_min_dir_above_threshold(node):
		nonlocal min_val
		nonlocal threshold
		for dirname in node.subdirs:
			subnode = node.subdirs[dirname]
			if subnode.size >= threshold and subnode.size < min_val:
				min_val = subnode.size
			if subnode.size >= threshold:
				find_min_dir_above_threshold(subnode)
	find_min_dir_above_threshold(root)
	print(min_val)