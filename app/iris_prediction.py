import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

correspondance = {0: "setosa", 1: "virginica", 2: "versicolor"}

iris_X, iris_y = datasets.load_iris(return_X_y=True)
np.unique(iris_y)


# Split iris data in train and test data
# A random permutation, to split the data randomly
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]

# Create and fit a nearest-neighbor classifier
knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)

def predict(data: list) -> str:
    try:
        result = knn.predict(data)
    except Exception as e:
        print(e)
        return "-1"
    return correspondance[result[0]]


if __name__ == "__main__":
    print(f"test data: {iris_X_test}")
    print(f"test predictions: {predict(iris_X_test)}")
    print(f"test real values: {iris_y_test}")