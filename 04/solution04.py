# Advent of Code
# 2022 Dec 4
import sys

def aoc1():
	count = 0
	for line in sys.stdin:
		pair = line.split(',')
		elf_1 = pair[0].split('-')
		elf_2 = pair[1].split('-')
		elf_1_start = int(elf_1[0])
		elf_1_end = int(elf_1[1])
		elf_2_start = int(elf_2[0])
		elf_2_end = int(elf_2[1])
		if elf_1_start == elf_2_start \
		or elf_1_start > elf_2_start and elf_1_end <= elf_2_end \
		or elf_1_start < elf_2_start and elf_1_end >= elf_2_end:
			count += 1

	print(count)

def aoc2():
	count = 0
	for line in sys.stdin:
		pair = line.split(',')
		elf_1 = pair[0].split('-')
		elf_2 = pair[1].split('-')
		elf_1_start = int(elf_1[0])
		elf_1_end = int(elf_1[1])
		elf_2_start = int(elf_2[0])
		elf_2_end = int(elf_2[1])
		if elf_1_start == elf_2_start \
		or elf_1_start > elf_2_start and elf_1_start <= elf_2_end \
		or elf_1_start < elf_2_start and elf_1_end >= elf_2_start:
			count += 1

	print(count)