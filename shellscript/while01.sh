#!/bin/sh

array=(0.255 0.8569 5.356 3.8521)
max=0
len=${#array[*]}
i=0

while [ $i -lt $len ]; do
    echo "$i: ${array[$i]}"
    val=`echo "${array[$i]}" `
    if [ $val -gt $max ]; then
        max=$val
    fi
    let i++
done
echo "MAX IS => $max"