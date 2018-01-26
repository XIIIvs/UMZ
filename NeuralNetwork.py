import tflearn
import numpy
import pandas


def str_column_to_float(data_set, column):
    for row in data_set:
        row[column] = float(ord(row[column]))


if __name__ == "__main__":
    train_file = '../train/train.tsv'
    dev_0_file = '../dev-0/in.tsv'
    test_a_file = '../test-A/in.tsv'

    data_frame_1 = pandas.read_csv(train_file, sep='\t')
    array_1 = data_frame_1.values
    data_frame_2 = pandas.read_csv(dev_0_file, sep='\t')
    array_2 = data_frame_2.values
    data_frame_3 = pandas.read_csv(test_a_file, sep='\t')
    array_3 = data_frame_3.values

    x_array = array_1[:, 1:4]
    y_array = array_1[:, 0]
    dev_0_array = array_2[:, 0:3]
    test_a_array = array_3[:, 0:3]

    for i in range(len(x_array[0])):
        str_column_to_float(x_array, i)
    for i in range(len(array_2[0])):
        str_column_to_float(array_2, i)
    for i in range(len(array_3[0])):
        str_column_to_float(array_3, i)

    label = numpy.array(y_array).reshape(1674, 1)

    net = tflearn.input_data(shape=[None, 3])
    net = tflearn.fully_connected(net, 64)
    net = tflearn.fully_connected(net, 32)
    net = tflearn.fully_connected(net, 16)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 4)

    linear = tflearn.fully_connected(net, 1, activation="linear")
    regression = tflearn.regression(linear, optimizer="sgd", metric="R2",
                                    loss="mean_square", learning_rate=0.01)
    model = tflearn.DNN(regression)
    model.fit(x_array, label, n_epoch=10, batch_size=16, show_metric=True)

    scores_1 = model.predict(dev_0_array)
    scores_2 = model.predict(test_a_array)

    output_dev_0 = open(r'../dev-0/out.tsv', 'w')
    for score in scores_1:
        print(score)
        output_dev_0.write(score + '\n')
    output_dev_0.write('e \n')
    output_dev_0.close()

    output_test_a = open(r'../test-A/out.tsv', 'w')
    for score in scores_2:
        print(score)
        output_test_a.write(score + '\n')
    output_test_a.write('e \n')
    output_test_a.close()
