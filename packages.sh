#!/bin/bash



#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
else
	apt install redis sqlite
fi
