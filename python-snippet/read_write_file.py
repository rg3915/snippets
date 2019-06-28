# python3
def read_file():
    with open('input.txt', 'rt') as f:
        print(f.read())


def read_lines():
    with open('input.txt', 'rt') as f:
        for line in f:
            print(line)


def write_file():
    with open('output.txt', 'w') as f:
        f.write('Hi there\n')
        f.write('Second line\n')
        f.close()


read_file()
read_lines()
write_file()
