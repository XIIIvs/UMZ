from csv import reader
from dataprocessing.DataPreprocessing import FixingShityInSet, FixingShityTrainSet
from sklearn.naive_bayes import GaussianNB
import numpy


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


if __name__ == "__main__":
    data_set_1 = data_load("train.tsv")
    data_set_2 = data_load("in.tsv")

    for i in range(len(data_set_1[0])):
        str_column_to_float(data_set_1, i)
    for i in range(len(data_set_2[0])):
        str_column_to_float(data_set_2, i)

    x_list = list()
    y_list = list()
    arg_1 = list()
    arg_2 = list()

    test_x_list = list()
    test_arg_1 = list()
    test_arg_2 = list()

    for data in data_set_1:
        arg_1.append(data[0])
        arg_2.append(data[1])
        y_list.append(data[2])
    x_list.append(arg_1)
    x_list.append(arg_2)

    for data in data_set_2:
        test_arg_1.append(data[0])
        test_arg_2.append(data[1])
    test_x_list.append(test_arg_1)
    test_x_list.append(test_arg_2)

    x_array = numpy.array(x_list).reshape((3601424, 2))
    y_array = numpy.array(y_list)
    test_x_array = numpy.array(test_x_list).reshape((134675, 2))

    gaussian_nb = GaussianNB()
    gaussian_nb.fit(x_array, y_array)
    GaussianNB(priors=None)
    predictions = gaussian_nb.predict(test_x_array)

    output = open(r'out.tsv', 'w')
    for prediction in predictions:
        if prediction == 10:
            prediction = "M"
        elif prediction == 20:
            prediction = "F"
        output.write(prediction + "\n")
        print(prediction)
    output.close()
