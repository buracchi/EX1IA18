import matplotlib.pyplot as plt
from pandas import read_csv
import numpy

def plot():

    names = ["swagDictionary"]  # "PyDictionary"] #filenames

    c = 0       #color
    for f in names:
        d = read_csv("../" + f + ".csv", sep = ',', header = None)  # read file
        #   d e' un dataframe: in pratica è una matrice. In d[i] c'è l'i-esima colonna
        x = d[0].values
        y = d[1].values
        plt.plot(x, y, color = "C" + str(c), label = f)
        plt.legend(loc = "best")
        #plt.savefig
        c += 1
    plt.savefig("dictSearch.png")
    plt.show()

def histogram():
    data = read_csv("../swagDictionary.csv", sep = ',', header = None)  # read file
    data = data[0]

    binNumber = max(int(round(numpy.log(max(data) - min(data)))), 25)

    #plt.hist(data, bins=range(min(data), max(data) + 10, (max(data) - min(data)) / binNumber), color='red')
    plt.hist(data, bins = binNumber, color = 'red')

    plt.xlabel("Time")
    plt.ylabel("Frequency")
    plt.title('Put here a title')

    plt.savefig('hist.png')

    plt.show()

if(__name__ == "__main__"):
    plot()
    histogram()
