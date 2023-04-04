e=1
while e<=12:
    print(e)
    e=e+1
print ("loop finish")

sum=0
g=1 
while g<=10 :
    sum=sum + g
    g=g+1
print (sum)

x=int(input("Enter the last term: "))
sum=0
g=1 
while g <= x:
    sum=sum + g
    g=g+1
print (sum)

i=1
while i <= 100:
    print (i)
    i = i+1
    if i==20:
        break
    
print("Hello")

i=1
while i <= 100:
    if i==20:
        continue
    print (i)
    i = i+1
print("Hello")