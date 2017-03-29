# Helper functions for python tutorials
import numpy as np

def package_dataset(file, x_train, y_train, x_test, y_test):
    """
    Bundle up the data into a form similar to Keras-style datasets
    :param file: Path to data file
    :param x_train: Array-like
    :param y_train:
    :param x_test:
    :param y_test:
    :return:
    """
    np.savez(file, ((x_train, y_train), (x_test, y_test)))


def unpackage_dataset(file):
    """
    Load in packaged data that was created with package_dataset
    :param file: Path to data file
    :return:
    """
    ((x_train, y_train), (x_test, y_test)) = np.load(file)['arr_0']
    return ((x_train, y_train), (x_test, y_test))
