#!/usr/bin/env python3

def initial_lanternfish_list(filename):
    with open(filename) as f:                           #Open the file and read the line
        lanternfishs = f.readline().strip().split(',')  
    return list(map(int, lanternfishs))                 #Return a list with the initial lanternfish list

def lanternfish(filename):
    lanternfishs = initial_lanternfish_list(filename)   #Initilize the lanternfish ages and number
    for day in range(80):                               #Iterate over 80 days
        new_fish = 0                                    #Number of fish to be born each day
        for i, fish in enumerate(lanternfishs):
            if fish == 0:                               #If a fish reaches the end of its cycle
                lanternfishs[i] = 6                     #It restarts the cycle at 6
                new_fish += 1                           #And a new fish is born
            else:
                lanternfishs[i] -= 1
        lanternfishs += [8]*new_fish                    #At the end of a day, we add newly born fish to the list
    return len(lanternfishs)                            #Return the total number of lanterfish


def main():
    with open("output.txt") as f:
        output = [int(x.strip()) for x in f.readlines()]
    for i, expected in enumerate(output):
        filename = f"input/input_{i + 1:02}.txt"
        result = lanternfish(filename)
        if result == expected:
            print(f"Correct result for case {i + 1}: {result}")
        else:
            print(f"Incorrect result for case {i + 1}: {expected} is " \
                f"expected, but {result} is returned")


if __name__ == "__main__":
    main()
