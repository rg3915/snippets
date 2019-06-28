#!/bin/bash
# for

for i in {1..20..2}; do
	let i=i*2
	echo "$i"
done

echo ""

for i in 1 7 10; do
	echo "$i"
done

echo "Nomes"
nome="Regis David Arthur Joao"
for n in $nome; do
	echo "$n"
done