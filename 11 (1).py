lst1=['name','english','python','math']
t=input().split()
stu={}
ilen=len(t)
for x in range(ilen):
    stu[lst1[x]]=t[x]
b=0
del t[0]
for x in t:
    c=int(x)
    b+=c
avg=b/len(t)
stu['avg']=avg
dic2=stu.copy()
del dic2['name']
lst5=list(dic2.values())
for x in range(len(lst5)):
    lst5[x]=int(lst5[x])
lst5.sort(reverse=True)
lst2=[]
for k,v in stu.items():
    if k!='name':
        lst2.append(v)
for x in range(len(lst2)):
    lst2[x] = float(lst2[x])
lst2.sort(reverse=True)
print(stu['name'],end=" ")
for x in range(len(lst2)):
    print("%.2f"%(lst2[x]),end=" ")
