from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import Normalizer
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

    x_array = array_1[:, 1:23]
    y_array = array_1[:, 0]

    for i in range(len(x_array[0])):
        str_column_to_float(x_array, i)
    for i in range(len(array_2[0])):
        str_column_to_float(array_2, i)
    for i in range(len(array_3[0])):
        str_column_to_float(array_3, i)

    scaler = Normalizer().fit(x_array)
    normalized_x = scaler.fit_transform(x_array)
    normalized_dev_0 = scaler.fit_transform(array_2)
    normalized_test_a = scaler.fit_transform(array_3)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(normalized_x, y_array)

    scores_1 = knn.predict(normalized_dev_0)
    scores_2 = knn.predict(normalized_test_a)

    output_dev_0 = open(r'../dev-0/out.tsv', 'w')
    for each in scores_1:
        print(each)
        output_dev_0.write(each + '\n')
    output_dev_0.write('e \n')
    output_dev_0.close()

    output_test_a = open(r'../test-A/out.tsv', 'w')
    for each in scores_2:
        print(each)
        output_test_a.write(each + '\n')
    output_test_a.write('e \n')
    output_test_a.close()