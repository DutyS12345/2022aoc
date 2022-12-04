#!/bin/bash

if [[ $# -ne 1 ]]; then
	echo "Usage: newday.sh <day>"
	exit
fi

if [[ ! -e $1 ]]; then
	echo "Creating $1/"
	mkdir $1
else
	echo "$1/ already exists"
fi

cd $1

if [[ ! -e solution$1.py ]]; then
	echo "Creating solution$1.py"
	cp ../template.py ./solution$1.py
	sed -i s/%s/$1/ ./solution$1.py
else
	echo "solution$1.py already exists"
fi

echo "Done"
# time python -c "import solution$1; solution$1.aoc$2()" < input.txt
