#QUESTION 1. 
name=input("Enter your name:")
print ("length:", len(name))
for i in range(len(name)):
    print(name)

#QUESTION 2.
n=int(input("Enter n:"))
print("sum=",sum(range(1 , n+1)))

#QUESTION 3.
num=int(input("Enter number:"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

#question 4.
n=int(input("Enter number:"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")            

#QUESTION 5.
n=int(input("Enter number:"))
if n==n[::-1]:
    print("parlidrome")
else:
    print("not parlidrome")
    