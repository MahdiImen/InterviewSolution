#!/usr/bin/env python3

def generator(filename):
    with open(filename) as f:   #Open the file and read each line
        for line in f:
            yield int(line.strip('')) #retrieve each depth measurement one at a time

def sonar(filename):
    n=0                                     #Initialize counter to 0
    gen = generator(filename)               #Create a generator to retrieve the depth measurements 
    try:        
        window_A = []                       #Create first window
        for i in range(3):                  #Get first three measurements
            window_A.append(next(gen))                           
        while(True):
            window_B = window_A[1:]         #Get the first and second measurements of the next window
            window_B.append(next(gen))      #Get the third measurement next window
            if sum(window_B)>sum(window_A) :#If the sum of the second window is bigger
                n += 1                      #We increase the counter
            window_A = window_B[:]      
    except StopIteration:                   #When the we reach the end of file, the generator raises a StopIteration. 
        return n                            #We then return the number obtained



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
