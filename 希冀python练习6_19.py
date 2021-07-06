def resultChange(a,b,c):
    return a*100 + b*10 + c

n, m = input().split(' ')
List1 = []
List2 = []
lastStr = ''
if ('.' in n) or ('.' in m):
    print("illegal input")
elif (0 <= int(n) <= 9) and (0 <= int(m) <= 9):
    n = int(n)
    m = int(m)
    if (n > m) or (m - n < 3):
        print("illegal input")
    else:
        for x in range(n, m):
            List1.append(x)
        iLen = len(List1)
        for x in range(iLen-2):
            for y in range(x+1,iLen-1):
                for z in range(y+1,iLen):
                    a = List1[x]
                    b = List1[y]
                    c = List1[z]
                    if a:
                        List2.append(resultChange(a,b,c))
                        List2.append(resultChange(a,c,b))
                    if b:
                        List2.append(resultChange(b,a,c))
                        List2.append(resultChange(b,c,a))
                    if c:
                        List2.append(resultChange(c,a,b))
                        List2.append(resultChange(c,b,a))
        List2.sort()
        for x in List2:
            lastStr += str(x) + ' '
        print(lastStr)
else:
    print("illegal input")