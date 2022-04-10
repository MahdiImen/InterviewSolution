#!/usr/bin/env python3
import numpy as np

def initial_lanternfish(filename):
    filedata = np.genfromtxt(filename , delimiter=',')
    filedata = filedata.astype('int64')
    l = [filedata[filedata == i].shape[0] for i in range(9)]
    return (l)


def lanternfish(filename, days):
  family = initial_lanternfish(filename)
  for day in range(days):
    new_born = family[0]
    family = np.hstack((family[1:],np.zeros(1,dtype='int64')))
    family[6] += new_born
    family[8] += new_born
  return family.sum()


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
