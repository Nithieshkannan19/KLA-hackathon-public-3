center = [0,0]



squaresize = 30

ssh = squaresize/2

diameter = 300

radius = diameter/2

nob = radius/squaresize

x,y = 0,0

arr =[]
arr.append([0,0,0,0])

q,p=0,0

while x <radius :
    x = x+squaresize
    q+=1
    #print(x,y,q,p)
    arr.append([x,y,q,p])
    
x,y = 0,0 
    
while x > (-radius) :
    x = x-squaresize
    q-=1
    #print(x,y,q,p)
    arr.append([x,y,q,p])
    
arr.sort()   
#print(arr)


arr2=[]
for i,j,q,p in arr :
    arr1 =[]
    arr1.append([i,j,q,p])
    
    while j <radius :
        j = j+squaresize
        p+=1
        #print(i,j,q,p)
        arr1.append([i,j,q,p])
        
    x,y = 0,0 
        
    while j > (-radius) :
        j = j-squaresize
        p-=1
        #print(i,j)
        arr1.append([i,j,q,p])
    arr1.sort()    
    #print(arr1)
    arr2.append(arr1)
    
    
arr2 = list(zip(*arr2))
print(arr2)

shift_vector = [10,10]

arr3 = []
for i in range(len(arr2)):
    arr4=[]
    for j in range(len(arr2[0])):
        inp = arr2[i][j]
        #print(arr2[i][j])
        #print(inp[0]-shift_vector[0])
        #print((inp[1]-shift_vector[1]))
        temp=[(inp[0]-shift_vector[0]),(inp[1]-shift_vector[1]),inp[2],inp[3]]
        #print(temp)
        arr4.append(temp)
    #print(arr4)
    arr3.append(arr4)
    
#print(arr3)

center1 = [center[0],center[1]-shift_vector[1]]

reference =[25,25]
r1 = [reference[0]//squaresize,reference[1]//squaresize]

arr5=[]
for i in range(len(arr3)):
    arr6=[]
    for j in range(len(arr3[0])):
        inp = arr2[i][j]
        temp=[inp[0],inp[1],inp[2]-r1[0],inp[3]-r1[1]]
        arr6.append(temp)
    arr5.append(arr6)
    #print(arr5)

#print(arr5)
   
f = open("demo21.txt", "w")

    
for i in range(len(arr5)):
    for j in range(len(arr5[0])):   
        inp1=arr5[i][j]
        a=inp1[0]
        b=inp1[1]
        c=inp1[2]
        d=inp1[3]
        f.write('('+str(c) + ',' + str(d)+') : ('+str(a)+','+str(b)+')')
        f.write("\n")

