# num2 =int( input ("Enter a number:"))
# result = 20/num2
# print(result)
# print("Done")
# try:
#    list = [20,0,30]
#    result = list [0]/list [3]
#    print (result)
#    print("Done")
# except ZeroDivisionError:
#    print ("Dividing by zero is not possible")
# finally:
#    print("Successful")

try:
   
   num1 = int(input("Enter First Number: ")) 
   num2 = int(input("Enter Second Number: ")) 
   result = num1/num2
   print(result)

except ValueError:
    print ("you have to insert only integer.")
except ZeroDivisionError:
   print("you can not divide a number by 0")

finally:
   print("thanks")