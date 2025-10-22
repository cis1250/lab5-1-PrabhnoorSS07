#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def getUserInput():
    while True:
        try:
            numTerms = int(input("Enter how many terms of the Fibonacci sequence you want: "))
            if numTerms > 0:
                return numTerms
            else:
                print("Error! Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def generateFibonacci(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def printSequence(seq):
    print("Fibonacci sequence:")
    for num in seq:
        print(num, end=" ")
    print()

def main():
    numTerms = getUserInput()
    fibonacciSeq = generateFibonacci(numTerms)
    printSequence(fibonacciSeq)
  
if __name__ == "__main__":
    main()
