my_dict={}   #Take a empty dic and ask  user to input to the number of time they want to enter and input
n=int(input("number of time want to enter"))                    # from the user to make dic.
for i in range(n):
    key= input("Enter key:")
    value=input("Enter value:")
    my_dict[key]=value
print("n Final dictionary:")
print(my_dict)

#question14.from weekly 1.assignement .
employee_details={
    101: {"name": "Riya", "department": "HR", "salary": 48000},
    102: {"name": "Neha", "department": "IT", "salary": 65000},
    103: {"name": "simran", "department": "Finance", "salary": 53000},
}
result=[]
for emp in employee_details.values():
    if emp['salary'] > 50000:
        result.append(emp["name"])
print(result)      

#QUESTION1.
    
   

