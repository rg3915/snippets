awk 'BEGIN {c=0} {if ( $0 ~ /Exemplo/ ) {c+=1; print $0c} else print $0}' exemplo.tex | tee exemplo1.tex
