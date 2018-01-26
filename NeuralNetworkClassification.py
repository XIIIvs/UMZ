import keras
import numpy
import pandas


def str_column_to_float(data_set, column):
    for row in data_set:
        row[column] = float(ord(row[column]))


def label_to_one_hot(data_set):
    label = list()
    for data in data_set:
        data = [1, 0] if data == 'e' else [0, 1]
        label.append(data)
    return label


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

    x_array = array_1[:, 1:23]
    y_array = array_1[:, 0]
    dev_0_array = array_2[:, 0:22]
    test_a_array = array_3[:, 0:22]

    for i in range(len(x_array[0])):
        str_column_to_float(x_array, i)
    for i in range(len(array_2[0])):
        str_column_to_float(array_2, i)
    for i in range(len(array_3[0])):
        str_column_to_float(array_3, i)
    y_array = label_to_one_hot(y_array)

    model = keras.models.Sequential()
    model.add(keras.layers.Dense(128, activation='relu', input_shape=(x_array.shape[1],)))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(256, activation='relu'))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(512, activation='relu'))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(1024, activation='relu'))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(512, activation='relu'))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(256, activation='relu'))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(128, activation='relu'))
    model.add(keras.layers.Dropout(0.2))
    model.add(keras.layers.Dense(units=2, activation='softmax'))
    model.summary()

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x_array, y_array, batch_size=128, epochs=10, verbose=1)

    scores_1 = model.predict(dev_0_array)
    scores_2 = model.predict(test_a_array)

    output_dev_0 = open(r'../dev-0/out.tsv', 'w')
    for score in scores_1:
        print(score)
        if score[0] > score[1]:
            score = 'e'
        else:
            score = 'p'
        print(score)
        output_dev_0.write(score + '\n')
    output_dev_0.close()

    output_test_a = open(r'../test-A/out.tsv', 'w')
    for score in scores_2:
        print(score)
        if score[0] > score[1]:
            score = 'e'
        else:
            score = 'p'
        print(score)
        output_test_a.write(score + '\n')
    output_test_a.close()
