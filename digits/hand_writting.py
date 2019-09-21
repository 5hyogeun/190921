import cv2
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import datasets, svm, metrics
from sklearn.metrics import accuracy_score

class HandWritting:
    def __init__(self):
        self._fname = datasets.load_digits()

    def read_file(self):
        plt.imshow(self.fname.images[0], cmap='gray')
        plt.show()

    def read_nums(self):
        digits = self._fname
        for i in range(15):
            plt.subplot(3, 5, i+1)
            plt.axis('off')
            plt.title(str(digits.target[i]))
            plt.imshow(digits.images[i], cmap='gray')
        plt.show()

    def learning(self):
        digits = datasets.load_digits()
        x = digits.images
        y = digits.target
        x = x.reshape((-1, 64)) # 2차원 배열 -> 1차원 배열로 변환
        x_trian, x_test, y_train, y_test \
            = train_test_split(x, y, test_size = 0.25)
        clf = svm.LinearSVC()
        clf.fit(x_trian, y_train)

        y_pred = clf.predict(x_test)
        print(accuracy_score(y_test, y_pred))

