#!/bin/bash

function printnumbers { echo ${ARRAY[*]}; }
function sortnumbers { ARRAY=( $(for i in ${ARRAY[@]}; do echo "$i"; done | sort -n) ); }

function average { echo "${ARRAY[@]}" | awk '{ for (i=1; i<=$NF; i++) total+=$i; } END { printf("%.2f\n", total/$NF); }'; }
function average2 { for i in ${ARRAY[@]}; do ((total+=$i)); done; echo $((total/${#ARRAY[@]})); }

function maximum { echo "${ARRAY[@]}" | awk '{ for (i=1; i<=$NF; i++) max=($i>max)?$i:max; } END { printf("%d\n", max); }'; }
function maximum2 { max=0; for i in ${ARRAY[@]}; do [ $i -gt $max ] && max=$i; done; echo "$max"; }

echo "Input number for sorting"
read -a ARRAY

echo "Number before sorting:"
printnumbers
sortnumbers

echo "Sorted number: "
printnumbers
echo "Average: $(average) or $(average2)"
echo "Maximum: $(maximum) or $(maximum2)"