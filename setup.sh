#!/bin/bash

present=$(pwd)
x=$present'/venv'

#echo "$x"

file=$x

if [ ! -d "$file" ]
then
        echo "Setting up the Environment"
	python3 -m venv venv

else
	echo "Environment Venv is already done"
fi


#exit()

echo "Stating the virtual env "
source venv/bin/activate

cd Main
echo "Installing the required packages"

pip3 install -r requirements.txt

echo "Setting up the Database"

python $present/Main/database.py
