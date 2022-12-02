#!/bin/bash

if [[ $# -ne 2 ]]; then
	echo "Usage: start.sh <day> <part>"
	exit
fi

cd $1
time python -c "import solution$1; solution$1.aoc$2()" < input.txt
