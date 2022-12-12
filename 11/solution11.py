# Advent of Code
# 2022 Dec 11
import sys
import re

def aoc1():
	monkeys = []
	def oper_func(operator, operand2):
		if operator == '*':
			if operand2 == 'old':
				return lambda x : x * x
			else:
				return lambda x : x * int(operand2)
		elif operator == '+':
			if operand2 == 'old':
				return lambda x : x + x
			else:
				return lambda x : x + int(operand2)
	def test_func(test_value):
		return lambda x : x % test_value == 0
	for line in sys.stdin:
		line = line.strip()
		if line == '':
			pass
		elif(match := re.match('Monkey (\\d+)', line)):
			monkey = {'throws' : 0}
			monkeys.append(monkey)
		elif(match := re.match('Starting items: (.*)', line)):
			monkey['items'] = [int(x) for x in match.group(1).split(', ')]
		elif(match := re.match('Operation: new = old ([*+]) (\\d+|old)', line)):
			monkey['operation'] = oper_func(match.group(1), match.group(2))
		elif(match := re.match('Test: divisible by (\\d+)', line)):
			monkey['test'] = test_func(int(match.group(1)))
		elif(match := re.match('If true: throw to monkey (\\d+)', line)):
			monkey['true'] = int(match.group(1))
		elif(match := re.match('If false: throw to monkey (\\d+)', line)):
			monkey['false'] = int(match.group(1))
		else:
			print('missed a line')
			print(line)

	def do_round():
		for monkey in monkeys:
			for i in range(len(monkey['items'])):
				worry = monkey['items'][i]
				worry = monkey['operation'](worry)
				worry = int(worry / 3)
				if monkey['test'](worry):
					monkeys[monkey['true']]['items'].append(worry)
				else:
					monkeys[monkey['false']]['items'].append(worry)
				monkey['throws'] += 1
			monkey['items'] = []
	for i in range(0, 20):
		do_round()
	max_throws_1 = 0
	max_throws_2 = 0
	for monkey in monkeys:
		if monkey['throws'] > max_throws_2:
			if monkey['throws'] > max_throws_1:
				max_throws_2 = max_throws_1
				max_throws_1 = monkey['throws']
			else:
				max_throws_2 = monkey['throws']
	print(max_throws_1 * max_throws_2)
	pass

def aoc2():
	monkeys = []
	cm = 1
	def oper_func(operator, operand2):
		if operator == '*':
			if operand2 == 'old':
				return lambda x : x ** 2
			else:
				return lambda x : x * int(operand2)
		elif operator == '+':
			if operand2 == 'old':
				return lambda x : x * 2
			else:
				return lambda x : x + int(operand2)
	def test_func(test_value):
		return lambda x : x % test_value == 0
	for line in sys.stdin:
		line = line.strip()
		if line == '':
			pass
		elif(match := re.match('Monkey (\\d+)', line)):
			monkey = {'throws' : 0}
			monkeys.append(monkey)
		elif(match := re.match('Starting items: (.*)', line)):
			monkey['items'] = [int(x) for x in match.group(1).split(', ')]
		elif(match := re.match('Operation: new = old ([*+]) (\\d+|old)', line)):
			monkey['operation'] = oper_func(match.group(1), match.group(2))
		elif(match := re.match('Test: divisible by (\\d+)', line)):
			monkey['test'] = test_func(int(match.group(1)))
			cm *= int(match.group(1))
		elif(match := re.match('If true: throw to monkey (\\d+)', line)):
			monkey['true'] = int(match.group(1))
		elif(match := re.match('If false: throw to monkey (\\d+)', line)):
			monkey['false'] = int(match.group(1))
		else:
			print('missed a line')
			print(line)
	def do_round():
		for monkey in monkeys:
			for i in range(len(monkey['items'])):
				worry = monkey['items'][i]
				worry = monkey['operation'](worry)
				worry %= cm
				if monkey['test'](worry):
					monkeys[monkey['true']]['items'].append(worry)
				else:
					monkeys[monkey['false']]['items'].append(worry)
				monkey['throws'] += 1
			monkey['items'] = []
	for i in range(0, 10000):
		do_round()
	max_throws_1 = 0
	max_throws_2 = 0
	for monkey in monkeys:
		if monkey['throws'] > max_throws_2:
			if monkey['throws'] > max_throws_1:
				max_throws_2 = max_throws_1
				max_throws_1 = monkey['throws']
			else:
				max_throws_2 = monkey['throws']
	print(max_throws_1 * max_throws_2)
	pass