# import heapq
nlift=int(input())
nfloor=int(input())

liftstatus=[]
for i in range(nlift):
    liftstatus.append([0,'up','open'])

    
arr=[]
for i in range(nlift):
    arr.append(input().split())
    
t=int(input())
se=input().split()

res=[0]*nlift

time=0
'''initial lift '''
while time<=t:
    for i in range(nlift):
        if liftstatus[i][1]!='null':
            res[i]+=1
            
        if int(arr[i][0])==liftstatus[i][0]:
            liftstatus[i][2]='open'
            if int(arr[i][1])>int(arr[i][0]):
                liftstatus[i][1]='up'
            else:
                liftstatus[i][1]='down'
                
            arr[i][0]=nfloor+1
                
        elif int(arr[i][1])==liftstatus[i][0] and int(arr[i][0])>nfloor:
            arr[i][1]=nfloor+1
            liftstatus[i][2]='open'
            liftstatus[i][1]='null'
        elif liftstatus[i][2]=='open':
            liftstatus[i][2]='close'
        else:
            if liftstatus[i][1]=='up':
                liftstatus[i][0]+=1
            elif liftstatus[i][1]=='down':
                liftstatus[i][0]-=1
    time+=1

'''lift selection'''

target=''
if int(se[0])>int(se[1]):
    target='down'
else:
    target='up'

targetlift=0
mndistance=float('inf')

for i in range(nlift):
    ls=liftstatus[i]
    
    if ls[1]=='null':
        temp=abs(ls[0]-int(se[0]))
        if temp==0:
            targetlift=i
            break
        elif mndistance>temp:
            tragetlift=i
            mndistance=temp
            
    elif ls[1]==target:
        if target=='down':
            temp=ls[0]-int(se[0])
            if temp==0:
                targetlift=i
                break
            elif temp<0:
                dd=ls[0]-int(arr[i][1])+2+(int(se[0]-int(arr[i][1])))
                if dd<mndistance:
                    targetlift=i
                    mndistance=dd 
            elif temp<mndistance:
                targetlift=i
                mndistance=temp 
        else:
            temp=ls[0]-int(se[0])
            if temp==0:
                targetlift=i
                break
            elif temp>0:
                dd=int(arr[i][1])-ls[0]+2+(int(arr[i][1])-int(se[0]))
                if dd<mndistance:
                    targetlift=i
                    mndistance=dd
            elif temp<mndistance:
                targetlift=i
                mndistance=temp 
    else:
        dd=abs(ls[0]-int(arr[i][1]))+2+abs(int(se[0])-int(arr[i][1]))
        if dd<mndistance:
            targetlift=i
            mndistance=dd
    
####

'''timer update'''
tt=0
if liftstatus[targetlift][1]=='null':
    tt=abs(liftstatus[targetlift][0]-int(se[0]))+2+abs(int(se[1])-int(se[0]))
elif target!=liftstatus[targetlift][1]:
    tt=abs(liftstatus[targetlift][0]-int(arr[targetlift][1]))+3+abs(int(se[0])-int(arr[targetlift][1]))+abs(int(se[1])-int(se[0]))
else:
    if target=='up':
        if liftstatus[targetlift][0]>int(se[0]):
            tt=2*int(arr[targetlift][1])-liftstatus[targetlift][0]-int(se[0])+3+abs(int(se[1])-int(se[0]))
        else:
            tt=max(int(se[1]),int(arr[targetlift][1]))+3
    else:
        if liftstatus[targetlift][0]<int(se[0]):
            tt=liftstatus[targetlift][0]-2*int(arr[targetlift][1])+int(se[0])+3+abs(int(se[1])-int(se[0]))
        else:
            tt=min(int(se[1]),int(arr[targetlift][1]))+3
res[targetlift]=tt+t-1
for i in range(nlift):
    if i!=targetlift:
        if int(arr[i][0])>nfloor:
            tt=abs(liftstatus[i][0]-int(arr[i][1]))+1-1
            res[i]+=tt
        else:
            tt=abs(liftstatus[i][0]-int(arr[i][0]))+abs(int(arr[i][0])-int(arr[i][1]))+2-1
            res[i]+=tt


###

print(liftstatus)
print(targetlift)
print(res)
# print(arr)