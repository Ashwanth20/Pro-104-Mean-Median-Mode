import csv
with open("HgtWgt.csv", newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)

newdata = []
for i in range(len(filedata)):
    n_num = filedata[i][1]
    newdata.append(float(n_num))

median = len(newdata)
newdata.sort()

if median % 2 == 0:
    median1 = float(newdata[median//2])
    median2 = float(newdata[median//2 - 1])
    median3 = (median1 + median2)/2
else:
    median3 = newdata[median//2]
    print(median)
print("Median is : " +str(median3))