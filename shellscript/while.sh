#!/bin/bash
# while

n=100
while [ $n != 0 ]
do
	let n-=10
	echo "$n"
done