

list_of_elements=list()
with open('ip.txt') as f:
    for line in f:
        list_of_elements.extend([int(x) for x in line.split()])

print list_of_elements[0]+list_of_elements[1]

print("1.addition")
print("2.sub")
print("3.mul")
print("4.div")
op=input("Enter your choice");

res=0 

f=open("op.txt","w+")

if op==1:
    res=list_of_elements[0]+list_of_elements[1]
elif op==2 :
    res=list_of_elements[0]-list_of_elements[1]
elif op==3:
    res=list_of_elements[0]*list_of_elements[1]
elif op==4:
    res=list_of_elements[0]/list_of_elements[1]
    


f.write(str(res))
print (res)

f.close()
    
