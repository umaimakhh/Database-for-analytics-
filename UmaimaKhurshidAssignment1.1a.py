'''Assigment No:1 - Q1
Name: Umaima Khurshid Ahmad
Date: 01/07/2021
'''

def inputUser():
    '''gets number string from the user'''
    return (input('Enter comma seprated numbers: ')) # returns user input returns only positive values

def mainStarter():
    '''main funcation'''
    totalAverage = commuteAverageOnNumbers(inputUser()) #value for average return from function 
    print(totalAverage) #for testing

def commuteAverageOnNumbers(commaSepratedNumbers):
    '''returns average of numbers'''
    return getNumbersFromString(commaSepratedNumbers)

def getNumbersFromString(commaSepratedNumbers):
    '''returns average of numbers'''
    total = 0
    count = 0 #keep track of total values in the list
    for numbers in commaSepratedNumbers.split(','): 
        total = int(numbers) + total
        count= count + 1
    average = total/count
    return (average) #returns average

mainStarter()