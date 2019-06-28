# Regis da Silva Santos

1. Eu ainda estou estudando Deploy, portanto considere somente o que eu escrevi no papel mesmo.

2. O código para o comando SQL é:

```
SELECT
    s.id, s.tstamp, s.value,
    IFNULL(value - (SELECT
        mt.diferenca
        FROM diferenca mt
        WHERE mt.id < m.id
        ORDER BY mt.id
        DESC LIMIT 0,1), 0) AS variation
    FROM sale s
    WHERE s.user_id = 1;
```

3 . O teste para a função em Python é:

```python
import unittest

anums = [1000, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rnums = "M D CD C XC L XL X IX V IV I".split()


def to_roman(x):
    ret = []
    for a, r in zip(anums, rnums):
        n, x = divmod(x, a)
        ret.append(r * n)
    return ''.join(ret)


class ToRoman(unittest.TestCase):

    def test_m(self):
        self.assertEqual(to_roman(1000), 'M')

    def test_d(self):
        self.assertEqual(to_roman(500), 'D')

    def test_cd(self):
        self.assertEqual(to_roman(400), 'CD')

    def test_c(self):
        self.assertEqual(to_roman(100), 'C')

    def test_xc(self):
        self.assertEqual(to_roman(90), 'XC')

    def test_l(self):
        self.assertEqual(to_roman(50), 'L')

    def test_xl(self):
        self.assertEqual(to_roman(40), 'XL')

    def test_x(self):
        self.assertEqual(to_roman(10), 'X')

    def test_ix(self):
        self.assertEqual(to_roman(9), 'IX')

    def test_v(self):
        self.assertEqual(to_roman(5), 'V')

    def test_iv(self):
        self.assertEqual(to_roman(4), 'IV')

    def test_i(self):
        self.assertEqual(to_roman(1), 'I')


if __name__ == '__main__':
    unittest.main()
```

5 . Fibonacci em Shell Script.

```bash
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
```