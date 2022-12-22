from pathlib import Path
import csv


def files(p):
    lista = []
    for x in p.iterdir():
        if x.is_file():
            lista.append(x)
    return lista


def csv_file(file):
    with open(file, newline='') as csvfile:
        fetch_file = csv.reader(csvfile, delimiter=',')
        tabla = []
        for row in fetch_file:
            # print(row)
            tabla.append(row)
    return tabla


def describe_csv(file, head):

    fname = result / file
    with open(fname, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(head)



data = Path(r'C:\Users\akans\PycharmProjects\Data') #The csv files in data folder
result = Path(r'C:\Users\akans\PycharmProjects\Output')


list = files(data)
print(list)
for f in list:
    f1 = str(f)


    ind = f1.rfind('\\')
    file = f1[(ind+1):]
    print('file', file)

    table = csv_file(f)


    head = [table[0]]
    print('head 1\n', head)
    head[0].append('Change')
    print('head 2\n',head)
    for i in range(1,len(table)):
        cambio = (float(table[i][4]) - float(table[i][1])) / float(table[i][1])

        table[i].append(str(cambio))

        head.append(table[i])


    describe_csv(file, head)



