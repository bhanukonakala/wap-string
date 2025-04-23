str1=input("enter the string:")
res=""
res1=""
for i in str1:
    if i>='A' and i<='Z':
        res=res+i
    if i>="a" and i<="z":
        res1=res1+i
        print(res+res1)


 #input: Great Learning
#output: GLreatearning