import numpy as np
import csv
import matplotlib.pyplot as plt

result = []


def Distance(x, y):
    a=np.array(x)-np.array(y)
    a=np.square(a)
    a=np.sqrt(sum(a))
    return a

def Mean(dataset):
    return sum(np.array(dataset)) / len(dataset)


def Get_center(dataset, k):
    temp = []
    while len(temp) < k:
        index = np.random.randint(0, len(dataset) - 1)
        if index not in temp:
            temp.append(index)
    return np.array([dataset[i] for i in temp])

def k_means(dataset, center, k):
    guocheng = []
    sum = 0
    for _ in range(k):
        temp = []
        guocheng.append(temp)
    for i in dataset:
        temp = []
        for j in center:
            temp.append(Distance(i, j))
        guocheng[temp.index(min(temp))].append(i)
    center_ = np.array([Mean(i) for i in guocheng])
    if (center_ != center).all():
        center = center_
        k_means(dataset, center, k)
    else:
        for i in range(len(center)):
            for j in range(len(guocheng[i])):
                sum += Distance(center[i], guocheng[i][j])
        result.append(sum)


def read_data(way):
    data = []
    with open(way, 'r') as file:
        lines = csv.reader(file)
        for row in lines:
            data.append(row)
    if way == 'iris.data':
        for x in range(len(data)):
            data[x] = data[x][:-1]
        for x in range(len(data)):
            for y in range(4):
                data[x][y] = float(data[x][y])
    elif way == 'haberman.data':
        for x in range(len(data)):
            data[x] = data[x][:-1]
        for x in range(len(data)):
            for y in range(3):
                data[x][y] = float(data[x][y])
    elif way == 'wine.data':
        for x in range(len(data)):
            data[x] = data[x][1:]
        for x in range(len(data)):
            for y in range(13):
                data[x][y] = float(data[x][y])
    elif way == 'breast-cancer-wisconsin.data':
        dele = []
        # print(len(data))
        for x in range(len(data) - 1):
            for y in range(10):
                if data[x][y] == '?':
                    dele.append(x)
        # print(dele)
        i = 0
        for x in dele:
            data.pop(x - i)
            i += 1
        for x in range(len(data)):
            data[x] = data[x][1:-1]
            for y in range(9):
                data[x][y] = float(data[x][y])
    elif way=='abalone.data':
        for x in range(len(data)):
            data[x] = data[x][1:]
        for x in range(len(data)):
            for y in range(8):
                data[x][y] = float(data[x][y])
    return data


def main(way):
    data = read_data(way)
    for k in range(2, 7):
        center = Get_center(dataset=data, k=k)
        k_means(dataset=data, center=center, k=k)
    x = [k for k in range(2, 7)]
    y = result
    plt.plot(x, y)
    plt.xlabel("k")
    plt.ylabel("sum")
    plt.title(way)
    plt.show()
    result.clear()


if __name__ == '__main__':
    iris = 'iris.data'
    bcw = 'breast-cancer-wisconsin.data'
    wine = 'wine.data'
    haberman = 'haberman.data'
    abalone='abalone.data'
    main(way=iris)
    main(way=haberman)
    main(bcw)
    main(wine)
    main(abalone)
