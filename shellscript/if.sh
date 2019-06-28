#!/bin/bash
# if

echo 'Digite um numero:'
read n
# o espaco depois de [ eh necessario
# ; antes de then tb
if  [ $n == 42 ]; then
	echo $n "ok"
else
	echo "Nao eh o numero."
fi