lList = input()
lList = lList.strip('[', ']')
iSum = int(0)
iLen = len(lList)
for x in range(iLen):
    iSum += int(lList[x])
fAve = iSum/iLen
sStr = str(fAve)
