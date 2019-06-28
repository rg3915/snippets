#!/bin/bash
# Funcao

# Comparação Numérica
# 	-lt		É menor que (LessThan)
# 	-gt		É maior que (GreaterThan)
# 	-le		É menor igual (LessEqual)
# 	-ge		É maior igual (GreaterEqual)
# 	-eq		É igual (EQual)
# 	-ne		É diferente (NotEqual)
# Comparação de Strings
# 	=		É igual
# 	!=		É diferente
# 	-n		É não nula
# 	-z		É nula
# Operadores Lógicos
# 	!		NÃO lógico (NOT)
# 	-a		E lógico (AND)
# 	-o		OU lógico (OR)
# ------------------------------------------------

v=(1 95 2 7 5 10 13 8 4)

function vetor(){
	echo ${v[*]}	# listando os itens do vetor
}

printf "v: "
vetor	# chamando a funcao

printf "Lendo vetor: "

function lendovetor(){
	for i in ${v[*]}
	do
		printf "%d " $i
	done
}

lendovetor

function soma(){
	x=$1
	y=$2
	echo $(( $x + $y))
}

printf "\nsoma: "
soma 5 10

function retorna(){
	return 42
}

valor=$(retorna)
echo "valor:" $?
echo $valor

function lista(){
	for i in $*
	do
		echo $i
	done
}

lista b a s h

printf "\nMaximo do vetor: "

function maximo(){
	max=${v[0]}
	n=${#v[*]}	# tamanho do vetor
	# c style
	for (( i=1; i < n; i++ ))
	do
		if  [ ${v[$i]} -ge $max ]; then # maior ou igual
			max=${v[$i]}
		fi
	done
	printf "%d\n" $max
}

maximo

#function media(){

#}

bubble_sort(){
        aux=0

        for (( a = 0 ; a < ${#v[*]} ; a++ ))
        do
                for (( b = 0 ; b < ${#v[*]} ; b++ )) 
                do
                        [[ ${v[$b]} -gt ${v[$a]} ]] && { aux=${v[$b]} ; v[$b]=${v[$a]} ; v[$a]=$aux ; }
                done
        done
}

bubble_sort

echo "Vetor ordenado: ${v[*]}"

function retorna(){
	printf 'Digite um numero: ' 
	read $1
}

retorna $1