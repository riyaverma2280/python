# 


# print("n Final dictionary:")
# print(my_dict)

# #question14.from weekly 1.assignement .
# employee_details={
#     101: {"name": "Riya", "department": "HR", "salary": 48000},
#     102: {"name": "Neha", "department": "IT", "salary": 65000},
#     103: {"name": "simran", "department": "Finance", "salary": 53000},
# }
# result=[]
# for emp in employee_details.values():
#     if emp['salary'] > 50000:
#         result.append(emp["name"])
# print(result)      

#QUESTION1.
# sentences = input("Enter a sentence: ")
# words = sentences.split()

# freq = {}

# for word in words:
#     freq[word] = freq.get(word, 0) + 1

# # sort dictionary by frequency (descending)
# sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

# print(sorted_freq)  

#QUESTION2.
# students = {
#     "Riya": 85,
#     "Reema":75,
#     "Neha":90,
#     "Muskan":88,
# }
# #a.
# total_marks=sum(students.values())
# average = total_marks / len(students) 
# print("average marks:",average)
# #b.
# print("\nStudents scoring above average:")
# for name , marks in students.items():
#     if marks > average:
#         print(name)
 
#Question3

# dict1 = {'a': 50, 'b': 30, 'c': 70}
# dict2 = {'b': 60, 'c': 65, 'd': 40}

# # Create an empty dictionary to store result
# merged_dict = {}

# # Add keys from dict1
# for key in dict1:
#     if key in dict2:
#         merged_dict[key] = max(dict1[key], dict2[key])
#     else:
#         merged_dict[key] = dict1[key]

# # Add remaining keys from dict2
# for key in dict2:
#     if key not in merged_dict:
#         merged_dict[key] = dict2[key]

# print(merged_dict)

#QUESTION4.
# my_dict={'name': 'Alice', 'city': 'Mohali', 'course':'Data Science'}
# max_len =0
# result_key=" "

# for key, value in my_dict.items():
#     if len(value)> max_len:
#         max_len = len(value)
#         result_key = key
# print(result_key)

# QUESTION5.

my_dict={'a':5, 'b':15, 'c':30, 'd':50, 'e':55}
filter_dict={k:v for k, v in my_dict.items() if 10<= v <= 50}
print(filter_dict)

#QUESTION6.







