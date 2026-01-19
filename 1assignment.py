# for i in range(1,50):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)

#Question2.
# for num  in range(2,101):
#     prime=True
#     for i in range(2,num):
#         if num%i==0:
#             prime=False
#             break
#         else:
#             print(num)
    
#Question3.
# score=int(input("Enter score:"))
# if score>=90:
#     print("grade A")
# elif score>=80:
#     print("Grade B")    
# elif score>=70:
#     print("Grade C")
# elif score>=60:
#     print("Grade D")
# else:
#     print("Grade F")
     
#QUESTION4.
# num=int(input("Enter number:"))
# for i in range(1,11):  
#   print(num,"x",i,"=",num*i)

#QUESTION5.
# Squares =[i*i for i in range(1,21) if i%2==0]
# print (Squares)

# #QUESTION6.
# year=int(input("Enter year:"))
# if year % 4==0:
#     print(" leap year")
# elif year % 100==0:
#     print("Not a Leap year")   
# elif year % 400==0:
#     print("Leap yaer") 
# else:
#     print("Not a  leap year")   

#QUESTION7.
# a = int(input("Side 1:"))
# b = int(input("Side 2:"))
# c = int(input("Side 3:")) 
# if a==b==c :
#   print ("Equilateral Triangle")  
# elif a==b or b==c or a==c:
#     print("Isosceles triangle") 
# elif a*a + b*b==c*c or b*b +c*c==a*a or a*a+ c*c==b*b:
#     print("Right Angle Triangle")      
# else:
#     print("Scalene Triangle")

#QUESTION8.
# num=int(input("Enter number"))
# if num >0:
#     print("Positive")
# elif num <0:
#     print("Negative")
# else:
#     print("Zero")   

#QUESTION10.
# weight= float(input("Enter your weight in kg:"))
# height= float(input("Enter your height in meters"))
# BMI= weight / (height * height)
# print("Your bmi is:", BMI)
# if BMI< 18.5:
#     print("underweight")
# elif BMI<24.9:
#     print("Normalweight")
# elif BMI<29.9:
#     print("overweights") 
# else:
#     print("Obesity")  

#QUESTION11.
    
# day=int(input("Enter day number:"))
# if day==1:
#   print("Monday")
# elif day==2:
#   print("Tuesday")
# elif day==3:
#   print("Wednesday")
# elif day==4:
#   print("Thursday")
# elif day==5:
#   print("Friday")
# elif day==6:
#    print("Saturday")
# elif day==7:
#   print("Sunday")
# else:
#    print("Invalid input")  

#QUESTION12
# price= float(input("Enter price:"))
# if price> 1000:
#   discount=price * 0.10  
# elif price>=500:
#   discount=price * 0.05
# else:
#   discount=0
# print("Discount:", discount)  
# print("Final price:", price - discount)   

#QUESTION13  sum of first n natural number
# n=int(input("Enter n: "))
# print("sum:",n*(n+1)//2)

#QUESTION15   count vowels
# s=input("Enter string:")
# count=sum(1 for ch in s.lower() if ch in "aeiou")
# print("vowels:", count)

#QUESTION16  sum of digits
# num=input("Enter number:")
# total=0
# for digit in num:
#     total +=int(digit)
#     print("sum of digits:",total)

#QUESTION17  star pattern
# for i in range(1,6):
#     print("*" *i)

#QUESTION19 even number till given number
n=int(input("enter number:"))
for i in range(2,n+1,2):
    print(i ,end=" ")


#QUESTION20  LIST OPERATIONS

