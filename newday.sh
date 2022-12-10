#!/bin/bash

if [[ $# -ne 1 ]]; then
	echo "Usage: newday.sh <day>"
	exit
fi

day=`printf '%02d' $1`

if [[ ! -e $day ]]; then
	echo "Creating $day/"
	mkdir $day
else
	echo "$day/ already exists"
fi

cd $day

if [[ ! -e solution$day.py ]]; then
	echo "Creating solution$day.py"
	cp ../template.py ./solution$day.py
	sed -i s/%s/$day/ ./solution$day.py
else
	echo "solution$day.py already exists"
fi

echo "Done"
# time python -c "import solution$1; solution$1.aoc$2()" < input.txt
