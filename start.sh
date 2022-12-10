#!/bin/bash

if [[ $# -ne 2 ]]; then
	echo "Usage: start.sh <day> <part>"
	exit
fi

day=`printf '%02d' $1`

cd $day
time python -c "import solution$day; solution$day.aoc$2()" < input.txt
