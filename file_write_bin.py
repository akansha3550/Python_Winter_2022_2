from file_read_csv import m
import _pickle

my_file = 'my_matrix.csv.dat'
with open(my_file, 'wb') as f:
    _pickle.dump(m, f)
