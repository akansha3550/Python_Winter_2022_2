from file_read_csv import m

my_out_file = 'my_matrix_out.csv'
with open(my_out_file, 'w') as f:
    for r in m:
        els = [str(i) for i in r ]
        print(els)
        line = '\t'.join(els)
        f.write(line + '\n')
