from collections import Counter
import csv
with open ("HgtWgt.csv", newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)

newdata = []
for i in range(len(filedata)):
    n_num = filedata[i][1]
    newdata.append(float(n_num))
mode = Counter(newdata)
modeRange = {
    "50-60" : 0,
    "60-70" : 0,
    "70-80" : 0
}

for height, occur in mode.items():
    if 50 < float(height) < 60:
        modeRange["50-60"] += occur
    elif 60 < float(height) < 70:
        modeRange["60-70"] += occur
    elif 70 < float(height) < 80:
        modeRange["70-80"] += occur

modeRanges,modeOccur = 0,0
for range, occurances in modeRange.items():
    if occurances > modeOccur:
        modeRanges, modeOccur = [int(range.split("-")[0]),int(range.split("-")[1])], occurances
mode2 = float((modeRanges[0] + modeRanges[1])/2)
print("Mode is : " +str(mode2))