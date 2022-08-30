o#!/bin/sh
#array_bash_allelem.sh

array=(one two three four)

echo "${array[@]}"
echo "${array[*]}"
IFS=':'
echo "${array[*]}"

IFS=$'\n'
echo "${array[*]}"
