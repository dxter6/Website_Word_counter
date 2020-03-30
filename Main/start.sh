#!/bin/bash

database='/tmp/database'
venv='venv'

if [ ! -d "$venv" ]
then
	echo "First run the Setup script"
else
	echo "Starting the rq worker  in background"
	source venv/bin/activate
	rq worker &
	python Main.py

fi


