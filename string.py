# program to get a string made of the first 2 and the last 2 chars from a given a string.If a length is less than 2 , return 'not valid string, instead of the empty string
def first_last_two(s):
    if len<2:
        return "not a valid string"
    return s[:2]+s[-2:]    #slicing  2 for first two ,-2 for last two


# Question2. swaping between two strings

def swap_first_two(a,b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a+ " " +  new_b


#Question3.
def add_ing_or_ly(s):  
    if len(s)<3:
        return s
    elif s.endswith("ing"):
        return s+"ly"
    else:
        return s+"ing" 
     

#Question4.    remove the nth index character from a non empty string
def remove_nth_char(s,n):   #n is index to remove
    if n<0 or n>= len(s):
        return "index out of range"
    return s[:n]+s[n+1:]

#example
string="python"
index = 4
result = remove_nth_char(string,index)
print(result) 
