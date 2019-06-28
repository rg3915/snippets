#! /bin/bash
vetor=( 2 1 3 4 5 )

bubble_sort(){
    aux=0

    for (( a = 0 ; a < ${#vetor[*]} ; a++ )); do
        for (( b = 0 ; b < ${#vetor[*]} ; b++ )); do
            [[ ${vetor[$b]} -gt ${vetor[$a]} ]] && { aux=${vetor[$b]} ; vetor[$b]=${vetor[$a]} ; vetor[$a]=$aux ; }
        done
    done
}

bubble_sort

echo "${vetor[*]}"