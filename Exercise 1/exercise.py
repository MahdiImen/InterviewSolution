#!/usr/bin/env python3


def generator(filename):
    with open(filename) as f:   #Open the file and read each line
        for line in f:
            yield int(line.strip('\n')) #retrieve each depth measurement one at a time

def sonar(filename):
    gen = generator(filename)   #Create a generator to retrieve the depth measurements 
    value_1 = next(gen)         #Get First measurement in the file
    n=0                         #Initialize counter to 0
    try:                        
        while(True):
            value_2 = next(gen) #Get the new measurement
            if value_2>value_1 :#If the new measurement is bigger
                n += 1          #We increase the counter
            value_1 = value_2      
    except StopIteration:       #When the we reach the end of file, the generator raises a StopIteration. 
        return int(n)           #We then return the number obtained

def main():
    with open("output.txt") as f:
        output = [int(x.strip()) for x in f.readlines()]
    for i, expected in enumerate(output):
        filename = f"input/input_{i + 1:02}.txt"
        result = sonar(filename)
        if result == expected:
            print(f"Correct result for case {i + 1}: {result}")
        else:
            print(f"Incorrect result for case {i + 1}: {expected} is " \
                f"expected, but {result} is returned")


if __name__ == "__main__":
    main()
