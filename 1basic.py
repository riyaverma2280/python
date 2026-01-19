print("Hello Riya")
print("i am learning python",end=" i am beginner ")
print("python class")

#  operator 
# i="hello22"
# a= input("enter value")
# a= int(input("enter value"))
# print("value of a is ",a)
# print(type(a))
 
# b=int(input("enter b"))
# print(a+b) 

# Arithmetic Operator
a=int(input("Enter a"))
b=int(input("Enter b"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)   # means a power of b 

# Assignment operator
a= 20
a+=10    #a=a+10=30
a-=15    #a=a-15=15
a*=10    #a=a*10=150
a/=15

print(a)

# Relational or comparsion operator   -- based on True or False

print(14>34)
print(34>=76)
print(45<17)
print(33!=45)
print(34<=67)
       
#logical operator
print(True or True or False)
print(True and True and True and False)

print(15>35 and 55>30)
print(55>30 or 42>46 or 87>23)

#Membership Operators     in, not in - True or False
print("Membership Operators")
Name="Riya Verma"
print("ur" in Name)
print("uri" not in Name)


# ID concept
i=10
j=10
print(id(i))
print(id(j))
print("------")
k='hi'
l="hi"
print(id(k))
print(id(l))

i=int(input("enter i "))
j=int(input("enter j "))
i=input("enter i")
j=input("enter j")
print(id(i))
print(id(j))

#IDENTITY OPERATOR   IS,IS NOT 
c=10
d=10
print( c is d)
