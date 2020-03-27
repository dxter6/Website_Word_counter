#!/bin/bash

present=$(pwd)
x=$present/venv

if [ -d "$x" ];then
	source "$x"/bin/activate
	cd "$present"/Main/ && set -m rq worker
	python "$present"/Main/Main.py
else
	echo "First run the Setup.sh"
fi

