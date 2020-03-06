import csv
import numpy as np
import math

def load_dataset(way):
    data = []
    with open(way, 'r') as file:
        lines = csv.reader(file)
        for row in lines:
            data.append(row)
    for x in range(len(data)):
        data[x] = data[x][:-1]
    for x in range(len(data)):
        for y in range(4):
            data[x][y]=float(data[x][y])
    return data


def distance(x, y):
    pingfanghe=0
    for i in range(len(x)):
        pingfanghe+=pow(x[i]-y[i],2)
    return float('{:.2f}'.format(math.sqrt(pingfanghe)))



def cluser_mean(data):
    sum=0
    mean=[]
    for x in range(4):
        for y in range(len(data)):
            sum+=data[y][x]
        mean.append(float('{:.2f}'.format(sum/len(data))))
        print(mean)
    return mean


def get_center(data, k):
    index = []
    center=[]
    while len(index)<k:
        x = np.random.randint(0, len(data) - 1)
        if x not in index:
            index.append(x)
    # print(index)
    for i in index:
        center.append(data[i])
    return center

def k_means(data,center,k):
    guocheng=[]
    for i in range(k):
        temp=[]
        guocheng.append(temp)
    for i in range(len(data)):
        temp=[]
        for j in range(len(center)):
            temp.append(distance(data[i],center[j]))
        # print(temp)
        # guocheng[temp.index(min(temp))].append(data[i])
        minindex=0
        for w in range(0,len(temp)):
            if(temp[w]<temp[minindex]):
                minindex=w
        guocheng[minindex].append(data[i])
    center_update=[]
    # print(guocheng)
    for i in range(k):
        center_update.append(cluser_mean(guocheng[i]))
    if center!=center_update:
        center=center_update
        k_means(data=data,center=center,k=k)
    # else:
    #     print('over')




def main(way):
    data = load_dataset(way=way)
    # print(data)
    k = 3
    center = get_center(data, k)
    # print(center)
    k_means(data=data, center=center,k=k)

if __name__ == '__main__':
    iris='iris.data'
    main(iris)
