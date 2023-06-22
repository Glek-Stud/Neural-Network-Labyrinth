from random import choices, shuffle
import tensorflow as tf
import numpy as np
from keras.layers import Dense
from keras import Sequential


class NeuralNetwork:
    def __init__(self):
        self.model = Sequential([
            Dense(64, activation='relu', input_shape=(4,)),
            Dense(4, activation='softmax')
        ])

        # Компиляция модели
        self.model.compile(optimizer='adam',
                           loss='categorical_crossentropy',
                           metrics=['accuracy'])

    @staticmethod
    def generate_dataset(count=500):

        sample = [0, 0, 0, 3, 3, 1, 1]
        all_dataset = []
        for i in range(count):
            arr = choices(sample, k=3) + [2]
            shuffle(arr)
            if 1 in arr:
                answer = arr.index(1) + 1
            elif 2 in arr:
                answer = arr.index(2) + 1
            else:
                answer = 5

            all_dataset.append([arr, answer])

        return tuple(all_dataset)

    @staticmethod
    def convert_to_right(dataset):
        # Підготовка даних
        features = np.array([data for data, _ in dataset]) / 10
        labels = np.array([label - 1 for _, label in dataset])  # Приведение меток к нумерации с 0

        # Перетворення міток в one-hot кодування
        labels = tf.keras.utils.to_categorical(labels, num_classes=4)

        return tuple([features, labels])

    def training(self, right_dataset, epochs=200):
        features, labels = right_dataset
        self.model.fit(features, labels, epochs=epochs)

    def auto_generate_training(self):
        gen_dataset = self.generate_dataset()
        right_dataset = self.convert_to_right(gen_dataset)
        self.training(right_dataset)

    def generate_ans(self, data):
        data = np.array([data]) / 10
        prediction = self.model.predict(data)
        predicted_label = np.argmax(prediction) + 1  # Приведення мітки до вихідної нумерації
        return predicted_label


if __name__ == '__main__':
    class_NeuralNetwork = NeuralNetwork()
    dataset_test = class_NeuralNetwork.generate_dataset()
    right_dataset_test = class_NeuralNetwork.convert_to_right(dataset_test)
    class_NeuralNetwork.training(right_dataset_test)
    ans = class_NeuralNetwork.generate_ans([0, 1, 1, 2])
    print(ans)
