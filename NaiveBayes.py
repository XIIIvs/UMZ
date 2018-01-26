from csv import reader


def data_load(filename):
    data_set = list()
    with open(filename) as file:
        csv_reader = reader(file, delimiter="\t")
        for row in csv_reader:
            if row:
                data_set.append(row)
    return data_set


def str_column_to_float(data_set, column):
    for row in data_set:
        try:
            row[column] = float(row[column].strip())
        except ValueError:
            if row[column] == 'diesel':
                row[column] = float(1)
            elif row[column] == 'benzyna':
                row[column] = float(2)
            elif row[column] == 'gaz':
                row[column] = float(3)
            else:
                s = row[column]
                q = ''.join(str(ord(c)) for c in s)
                row[column] = float(q)

