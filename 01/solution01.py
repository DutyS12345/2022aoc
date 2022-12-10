# Advent of Code
# 2022 Dec 1
import sys

def aoc1():
	next_elf_cal = 0
	max_elf_cal = 0
	
	for line in sys.stdin:
		line = line.strip()
		if line == "":
			if max_elf_cal < next_elf_cal:
				max_elf_cal = next_elf_cal
			next_elf_cal = 0
		else:
			next_elf_cal += int(line)

	print(max_elf_cal)

def aoc2():
	next_elf_cal = 0
	max_elf_cal_t1 = 0
	max_elf_cal_t2 = 0
	max_elf_cal_t3 = 0
	for line in sys.stdin:
		line = line.strip()
		if line == "":
			if max_elf_cal_t3 < next_elf_cal:
				if max_elf_cal_t2 < next_elf_cal and max_elf_cal_t2 <= max_elf_cal_t1:
					max_elf_cal_t3 = max_elf_cal_t2
					max_elf_cal_t2 = next_elf_cal
				elif max_elf_cal_t1 < next_elf_cal and max_elf_cal_t1 <= max_elf_cal_t2:
					max_elf_cal_t3 = max_elf_cal_t1
					max_elf_cal_t1 = next_elf_cal
				else:
					max_elf_cal_t3 = next_elf_cal

			next_elf_cal = 0
		else:
			next_elf_cal += int(line)

	print(max_elf_cal_t1 + max_elf_cal_t2 + max_elf_cal_t3)
