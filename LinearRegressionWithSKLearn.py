from sklearn import linear_model
import numpy


def for_one_arg():
    flats_x = list()
    flats_y = list()
    flats_x_test = list()

    file_1 = open("train.tsv")
    file_2 = open("in.tsv")

    for line in file_1:
        line = line.split()
        flats_x.append(float(line[5]))
        flats_y.append(float(line[0]))

    for line in file_2:
        line = line.split()
        flats_x_test.append(float(line[4]))

    reshaped_x = numpy.array(flats_x).reshape(len(flats_x), 1)
    reshaped_y = numpy.array(flats_y)
    reshaped_x_test = numpy.array(flats_x_test).reshape(len(flats_x_test), 1)

    regression = linear_model.LinearRegression()
    regression.fit(reshaped_x, reshaped_y)

    flats_y_predictons = regression.predict(reshaped_x_test)

    output = open("out.tsv", "w")
    for prediction in flats_y_predictons:
        output.write(str(prediction) + '\n')
        print(prediction)


def for_many_args():
    flats_x = list()
    flats_y = list()
    flats_x_test = list()
    x2 = list()
    x3 = list()
    x5 = list()
    x1_test = list()
    x2_test = list()
    x4_test = list()

    file_1 = open("train.tsv")
    file_2 = open("in.tsv")

    for line in file_1:
        line = line.split()
        x2.append(float(line[2]))
        x3.append(float(line[3]))
        x5.append(float(line[5]))
        flats_y.append(float(line[0]))

    flats_x.append(x2)
    flats_x.append(x3)
    flats_x.append(x5)

    for line in file_2:
        line = line.split()
        x1_test.append(float(line[1]))
        x2_test.append(float(line[2]))
        x4_test.append(float(line[4]))

    flats_x_test.append(x1_test)
    flats_x_test.append(x2_test)
    flats_x_test.append(x4_test)

    reshaped_x = numpy.array(flats_x).reshape((1674, 3))
    reshaped_y = numpy.array(flats_y)
    reshaped_x_test = numpy.array(flats_x_test).reshape(150, 3)

    regression = linear_model.LinearRegression()
    regression.fit(reshaped_x, reshaped_y)

    flats_predictions = regression.predict(reshaped_x_test)

    output = open("out_many.tsv", "w")
    for prediction in flats_predictions:
        output.write(str(prediction) + '\n')
        print(prediction)


if __name__ == "__main__":
    for_one_arg()
    for_many_args()
