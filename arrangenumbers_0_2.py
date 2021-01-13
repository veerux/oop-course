'''
Arrange Numbers -game where the user tries to arrange the numbers in a
3x3 table so that they are sorted from smallest to largest. 
@author: Veera Määttänen
'''


def swapPositions(numbers, pos1, pos2):
    numbers[pos1], numbers[pos2] = numbers[pos2], numbers[pos1]
    return numbers

numbers = ['4', '7', '2', '6', '8', '3', '5', '_', '1']
check = ('1', '2', '3', '4', '5', '6', '7', '8', '_' )


print("8 puzzle - arrange the numbers by swapping with the empty place")
print(numbers)



while tuple(numbers) != check : 
    number = input("number to move: ")
    first = numbers.index(number)
    second = numbers.index('_')
    swapPositions(numbers, first, second)
    print(numbers)



print(numbers)
print("The numbers are in the correct order")


