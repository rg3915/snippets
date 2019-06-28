echo 'file1.txt'
cat file1.txt

# insert text in first line
sed '1,1 s/^/abcdef\n/' < file1.txt > file2.txt

echo 'file2.txt'
cat file2.txt
