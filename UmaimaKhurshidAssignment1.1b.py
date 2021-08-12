'''Assigment No:1 - Q2
Name: Umaima Khurshid Ahmad
Date: 01/07/2021
'''

def mainProgram():
    '''main program that gets number string from the user'''
    tableName = (input('Enter table name: ')) # returns user input for table name
    parameterValues = input('Enter parameters to insert in %s: '%tableName)
    parameterList = genrateListForParametersValue(parameterValues)
    queryStatement = generateInsert(tableName,genrateListBackToString(parameterList))
    print(queryStatement)

def genrateListForParametersValue(parameterValues):
    '''returns list of comma seprated values'''
    parameterList = []
    for listIndex in parameterValues.split(','):
        parameterList.append(listIndex)
    return parameterList

def genrateListBackToString(parameterList):
    '''returns string of comma seprated values from list - as requiremnt in example
    Input Parameter: 
    parameterList : list - format [1, Jane, A+])'''
    parameterString =' , '.join(parameterList)
    return parameterString

def generateInsert(tableName,parameterString):
    '''returns the statment for SQL
    Input Parameter: 
    tableName : name of the table
    parameterList : values inside the table - format (1, Jane, A+))'''
    tableInsert = generateTableInsert(tableName)
    ValueInsert = genrateValueInsert(parameterString)
    return tableInsert + ValueInsert

def generateTableInsert(tableName):
    '''returns SQL statment for insert'''
    return 'INSERT INTO %s' %tableName

def genrateValueInsert(parameterString):
    '''returns SQL statment for Values'''
    return ' VALUES ( %s )' %parameterString

mainProgram()
