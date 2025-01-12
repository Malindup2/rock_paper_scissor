#activity1
tot=0.0
max=-float("inf")
min=float("inf")
for i in range(10):
    marks=int(input("Enter the Marks"))
    tot+=marks

    if marks>max:
        max=marks
    if marks<min:
        min=marks

print("Max",max)
print("Min",min)
print("Avg",tot/10.0)



#activity2
marks=int(input("Enter the student marks"))
if(marks>75):
    print('A')
elif (marks>=65):
    print('B')
elif(marks>=55):
    print('C')
elif(marks>=45):
    print('S')
else:
    print('F')


#activity3
  tot=0
    while True:
       num=int(input("Enter the number"))
       if(num==-999):
        break
    tot+=num
   print("Tot is:",tot)