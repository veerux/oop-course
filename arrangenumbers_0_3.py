'''
Arrange Numbers -game where the user tries to arrange the numbers in a
3x3 table so that they are sorted from smallest to largest. 

imports 
imports

@author: Veera Määttänen
'''

import random

def main():
    '''
        
    The main program
    
    '''

    numbers = isSolvable()   
    check = ('1', '2', '3', '4', '5', '6', '7', '8', '_' )

    print("8 puzzle - arrange the numbers by swapping with the empty place")
    print(numbers)

    while tuple(numbers) != check : 
        number = input("number to move: ")
        first = numbers.index(number)
        second = numbers.index('_')
        swapPositions(numbers, first, second)
        print(numbers)

    print("The numbers are in the correct order!")


def swapPositions(numbers, pos1, pos2):
    '''
    
    Function for swapping the positions of the numbers. 
    
    '''
    
    numbers[pos1], numbers[pos2] = numbers[pos2], numbers[pos1]
    return numbers



def isSolvable():
    '''
    
    To check that the numbers are in a solvable order. 
    Returning a solvable list. 
    
    '''
    
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '_']
    
    while True:
        random.shuffle(numbers)
        invCount = 0
        for i in range(8):
            for j in range(9):
                if (numbers[j] and numbers[i] and numbers[i] > numbers[j]):
                    invCount += 1
        if invCount % 2 == 0:
            break  
          
    return numbers
    

main()

