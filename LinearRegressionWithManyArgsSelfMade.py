from random import seed
from csv import reader


def data_load(filename):
    data_set = list()
    with open(filename) as file:
        csv_reader = reader(file, delimiter="\t")
        for row in csv_reader:
            if row:
                data_set.append(row)
    return data_set


def switch_ones_column(data_set):
    for each in data_set:
        index = 0
        while index < 5:
            thing = each.pop(0)
            each.append(thing)
            index += 1


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


def price_column(data_set):
    for row in data_set:
        price = row.pop(0)
        row.append(price)


def del_mark1(data_set):
    for row in data_set:
        row.pop(3)


def del_mark2(data_set):
    for row in data_set:
        row.pop(2)


def data_set_min_max(data_set):
    list_min_max = list()
    for index in range(len(data_set[0])):
        col_values = [row[index] for row in data_set]
        value_min = min(col_values)
        value_max = max(col_values)
        list_min_max.append([value_min, value_max])
    return list_min_max


def normalize_data_set(data_set, min_max):
    for row in data_set:
        for index in range(len(row)):
            row[index] = (row[index] - min_max[index][0]) / (min_max[index][1] - min_max[index][0])


def predict(row, coefficients):
    y_hat = coefficients[0]
    for index in range(len(row)-1):
        y_hat += coefficients[index + 1] * row[index]
    return y_hat


def coefficients_sgd(train, l_rate, n_epochs):
    coefficient = [0.0 for index in range(len(train[0]))]
    for epoch in range(n_epochs):
        sum_error = 0
        for row in train:
            y_hat = predict(row, coefficient)
            error = y_hat - row[-1]
            sum_error += error**2
            coefficient[0] = coefficient[0] - l_rate * error
            for index in range(len(row)-1):
                coefficient[index + 1] = coefficient[index + 1] - l_rate * error * row[index]
        print("Epoch= ", epoch, ", lrate=", l_rate, ", error=", sum_error)
    return coefficient


def linear_regression_sgd(train, test, l_rate, n_epoch):
    predictions = list()
    coefficient = coefficients_sgd(train, l_rate, n_epoch)
    print(coefficient)
    for row in test:
        y_hat = predict(row, coefficient)
        predictions.append(y_hat)
    return predictions


if __name__ == "__main__":
    print("self-made Linear Regression")

    seed(1)

    data_set_1 = data_load("train.tsv")
    data_set_2 = data_load("in.tsv")

    del_mark1(data_set_1)
    del_mark2(data_set_2)
    price_column(data_set_1)

    for i in range(len(data_set_1[0])):
        str_column_to_float(data_set_1, i)
    for i in range(len(data_set_2[0])):
        str_column_to_float(data_set_2, i)

    minmax = data_set_min_max(data_set_1)
    normalize_data_set(data_set_1, minmax)

    for i in range(len(data_set_1)):
        data_set_1[i].append(1)

    switch_ones_column(data_set_1)

    for data in data_set_1:
        print(data)

    scores = linear_regression_sgd(data_set_1, data_set_2, l_rate=0.01, n_epoch=50)

    output = open("out.tsv", "w")
    for score in scores:
        output.write(str(score) + "\n")
        print(score)
    output.close()
