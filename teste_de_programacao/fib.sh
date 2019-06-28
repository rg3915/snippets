#!/bin/bash

if [ $# -eq 1 ]; then
    num=$1
else
    echo -n "Enter a number:"
    read num
    fi

f1=0
f2=1
echo "$num"

for (( i=0; i<=num; i++ )); do
    echo -n "$f1 "
    fn=$((f1+f2))
    f1=$f2 f2=$fn
done

echo