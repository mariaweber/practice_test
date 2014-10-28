#!/bin/bash
# This script takes the first and second input after the program name
# These names are then searched for in the specific directory
# The output is the number of lines in which this word was found in the files
#  in the directory

VAR1=$(grep -w $1 /Users/mariaweber/dirac_drive_test/* | wc -l)
VAR2=$(grep -w $2 /Users/mariaweber/dirac_drive_test/* | wc -l)

echo $1 $VAR1
echo $2 $VAR2
