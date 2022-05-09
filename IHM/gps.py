import numpy as np
import matplotlib.pyplot as plt
import pynmeagps as nmea


def np_open(filename):
    """Open a file and return a numpy array."""
    # data = np.loadtxt(filename, delimiter=',', dtype=str)
    return np.loadtxt(filename, delimiter='\n', dtype=str)


def select_data(data):
    L = [line.split(',') for line in data]
    res = []
    for line in L:
        if line[0] == '$GPGGA':
            res.append(line)
    return res


def plot_data(data):
    lat = []
    lon = []
    for line in data:
        lat.append(float(line[2]))
        lon.append(float(line[4]))
    plt.plot(lat, lon)
    plt.show()


if __name__ == '__main__':
    print(np_open('data/data_uv24.nmea'))
    data = np_open('data/data_uv24.nmea')
    print(select_data(data))
    plot_data(select_data(data))