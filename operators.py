# Input student details
name = input("Enter student name: ")
student_class = input("Enter class: ")
section = input("Enter section: ")

# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    mark = int(input("Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate total and percentage
total = sum(marks)
percentage = total / 5

# Display result
print("\n--- Student Result ---")
print("Name:", name)
print("Class:", student_class)
print("Section:", section)
print("Percentage:", percentage, "%")
#QUESTION2 Input 3 Numbers and Return Their Sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

total = a + b + c
print("Sum:", total)

#QUESTION 3 Input a Number and Return Its Square
num = int(input("Enter a number: "))
square = num * num
print("Square of the number:", square)

4️⃣ Celsius to Fahrenheit Conversion
# Take temperature as string input
celsius_str = input("Enter temperature in Celsius: ")

# Convert to float
celsius = float(celsius_str)

# Convert to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Display result
print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)
5️⃣ Quotient and Remainder Program
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

quotient = num1 // num2
remainder = num1 % num2

print("Quotient:", quotient)
print("Remainder:", remainder)
6️⃣ Simple Interest Program
Formula:
SI = (P × R × T) / 100

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest: "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100

print("Simple Interest:", SI)
If you want, I can:

Combine all of these into one menu-based program

Rewrite them using functions

Simplify them for school-level answers

Add sample input/output

Just tell me 🙂

