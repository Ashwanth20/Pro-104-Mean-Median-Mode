import csv
with open("HgtWgt.csv", newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)

newdata = []
for i in range(len(filedata)):
    n_num = filedata[i][1]
    newdata.append(float(n_num))

mean = len(newdata)
sum = 0
for x in newdata:
    sum += x

meanvalue = sum/mean
print("Mean/Average is : " + str(mean))