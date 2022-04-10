#!/usr/bin/env python3
import numpy as np

def initial_lanternfish(filename):
    filedata = np.genfromtxt(filename , delimiter=',')
    filedata = filedata.astype('int64')
    initial_fish_distribution = [filedata[filedata == i].shape[0] for i in range(9)] #Fish distrubution by days left till giving birth ranging from 0 to 8
    return (initial_fish_distribution)


def lanternfish(filename, days):
    #Get the initial distribution of lanternfish by age
    fish_distribution = initial_lanternfish(filename) 
    for day in range(days):
        #Number of new born fish: For each fish of age 0 one more fish will be born
        new_born = fish_distribution[0]
        #New distribution :
        fish_distribution = np.hstack((fish_distribution[1:],np.zeros(1,dtype='int64')))
        fish_distribution[6] += new_born #Fish that gave birth will now return to 6
        fish_distribution[8] += new_born #New born fish start at 8
    return fish_distribution.sum()


def main():
    with open("output.txt") as f:
        output = [int(x.strip()) for x in f.readlines()]
    for i, expected in enumerate(output):
        filename = f"input/input_{i + 1:02}.txt"
        result = lanternfish(filename,80)
        if result == expected:
            print(f"Correct result for case {i + 1}: {result}")
        else:
            print(f"Incorrect result for case {i + 1}: {expected} is " \
                f"expected, but {result} is returned")


if __name__ == "__main__":
    main()
