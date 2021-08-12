filePath = 'E:\DPU\winter 2020\\output_FuncationalDependacy_4e.txt'

fd = open(filePath, 'r')
print("\nReading file lines... /n")
allData = fd.readlines()
course = {}
voilationName=""

funcationalDependacyDectected = False
for line in allData:
    values = line.split(',')
    if values[4] not in course.keys():
        course[values[4]] = values[6]
    else:
        if values[6] != course[values[4]]:
            funcationalDependacyDectected = True
            voilationName = values[4]
if  funcationalDependacyDectected:
                print("Funcational Dependacy voilation dectected in :"+voilationName)
else:
    print("Funcational Dependacy voilation not dectected")











