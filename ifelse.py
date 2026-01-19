#Question 1  Wap userto input a number and then month name corresponding to that number

num = int(input("Enter the Month Number (1-12) "))

if num == 1:
    print("January")
elif num == 2:
     print("February")
elif num == 3:
    print("March")
elif num == 4:
     print("April")
elif num == 5:
     print("May") 
elif num == 6:
    print("June") 
elif num == 7:
    print("July")
elif num == 8:
     print("August")   
elif num == 9:
    print("September")         
elif num == 10:
    print("October")
elif num == 11:
    print("November")  
elif num == 12:
    print("December")   
else :
    print("Invalid month number")       



# Question2  wap ask user to input 2 number
a= int(input("Enter First Number"))
b=int(input("Enter Second number"))
 #1. Both number are equl or not 
if a == b:
    print("Both number are equal")
else:
    print("Both number are not equal")    

#2. Which is bigger in both 
if a > b :
    print("First number is bigger")
elif b > a :
     print("Second number is bigger")   
else:
    print ("Both are equal")   

#3. Either first number is smaller or equal to second number
if a<=b:
     print("First number is smaller or equal to second number")
else:
    print("First number is greater than second number")      

#4. Print name based on condition
if a>b:
    for i in range(4):
       print("Riya")
elif a<b:
  for i in range(5):
      print("verma")      
  

#Question3. using user input ask user to input 2 string and tell followings
s1=input("Enter first string:")
s2=input("Enter second string:")

#1 using == tell both string equal or not 
if s1 == s2:
  print("string are equal using ==")
else:
    print("strings are not equal using== ")

#Question4. Input 2 string , convert into number and compare using is op tell both are equal or not

s1=input("Enter first number as string:")
s2=input("Enter the second number as string:")

n1=int(s1)
n2=int(s2)
if n1 is n2: 
    print("Both number are equal using is")
else:
    print("Both number are not equal using is") 



#Question5. Python program to calculate the sum of all numbers from 1 to a given number

n=int(input("Enter a number:"))
total=0
for i in range(1, n+1):
  total = total+i 
print("sum =", total)

# #Question6. Print all even number up to given number

n=int(input("Enter a number:"))
print ("Even number are:")
for i in range(2, n+1):
  if i%2==0:
     print(i,end=" , ")

#Question7. user to input a number and with +or - and perform following output

n=int(input("Enter a number:"))
op=input("Enter operator (+ or  -):")

if op =="+":
  for i in range (0 , n):
    print(i,end=",")
elif op=="-":
  for i in range (n,0,-1):
    print(i, end=",")
else:
  print("Invalid operator")        
  




