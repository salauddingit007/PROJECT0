# Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


print((lambda a,b : a*a + 2*a*b + b*b)(2,3))

a=(lambda x :x*x*x)(2)
print (a)