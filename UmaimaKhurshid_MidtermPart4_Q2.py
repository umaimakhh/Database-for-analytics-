filePath = 'E:\DPU\winter 2020\\output.txt'

fd = open(filePath, 'r')
print("\nReading file lines... /n")
allData = fd.readlines()

course = {}
departmentName = []
for line in allData:
    listInsert = []
    values = line.split(',')
    if values[5] == ' None' or values[3] == ' None':
        pass
    else:
        if values[5] not in course.keys():
            course[values[5]]= values[3]
        else:
            listInsert = course.get(values[5])
            gradyear = int(listInsert)
            if(gradyear >= int(values[3])):
                course[values[5]]= values[3]
    
print(course)


