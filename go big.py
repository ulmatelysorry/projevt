t = input()
List = []
while t != '':
    t = t.split(' ')
    List.append([float(t[0]), float(t[1])])
    t = input()
fSum = 0
fCount = 0
for x in List:
    fSum += x[0]*x[1]
    fCount += x[1]
print("%.4f"%(fSum/fCount))