from file_read_csv import m
my_file = 'my_matrix.csv'
with open(my_file, 'w')as f:
    for r in m:
        els = [str(i) for i in r]
        print(els)
        line = '\t'.join(els)
        f.write(line + '\n')