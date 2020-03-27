#!/bin/bash

x=$(pwd)
x=$x'/venv'
echo "$x"

file=$x

if [ -d "$file" ];then
	echo "yes $file"
fi
