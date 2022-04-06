#!/usr/bin/env python3

def initial_lanternfish_list(filename):
    with open(filename) as f:                           #Open the file and read the line
        lanternfishs = f.readline().strip().split(',')  
    return list(map(int, lanternfishs))                 #Return a list with the initial lanternfish list

#The following recursive function will calculate the 
#number of grandchildren of one fish of age 6 after
# a given number of days 
def grandchildren(days_left): 
  if days_left < 7:
    return 0
  fish_born = 0
  for i in range(days_left//7):
    fish_born += grandchildren(days_left-2-(i+1)*7)
  return fish_born + (days_left // 7)


def lanternfish(filename):
    #Initilize the lanternfish ages and number
    lanternfishs = initial_lanternfish_list(filename) 
    #There are 6 ages possibles for the initial state : [0,1,2,3,4,5,6]  
    #For each age, we will determine how much one fish at that age can
    #have as grandchildren after 80 days
    #PS1: The number of grandchildren of a fish of age n on day d
    #is the same on the day d+(6-n)
    #PS2: The function grandchildren assumes that the fish is of age 6
    grandchildren_born = list(map(grandchildren, [86,85,84,83,82,81,80] )) 
    #The initial number of lanternfish
    n = len(lanternfishs)
    #For each lanternfish in the initial list we add the total number of 
    #its grandchildren after 80 days 
    for fish in lanternfishs:
        n += grandchildren_born[fish]
    #Return the total number of lanterfish
    return n                           

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
