# program to get a string made of the first 2 and the last 2 chars from a given a string.If a length is less than 2 , return 'not valid string, instead of the empty string
s = "Coder roots"

if len(s) < 2:
    print("not a valid string")
else:
    result = s[:2] + s[-2:]  #slicing
    print(result)
# Question2. swaping between two strings

s1 = "coder"
s2 = "roots"

new_s1 = s2[0] + s1[1:]
new_s2 = s1[0] + s2[1:]

print(new_s1 + " " + new_s2)


# #Question3.
s = "string"

if len(s) < 3:
    print(s)
elif s.endswith("ing"):
    print(s + "ly")
else:
    print(s + "ing")
     

# #Question4.    remove the nth index character from a non empty string
s="python"
n=2

result=s[:n]+s[n+1:]
print(result)