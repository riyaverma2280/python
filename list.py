#create a list with 5 friends
friends = ["A","B","C","D","E"]
print("friends list:",friends)
 #add raju at the end
friends.append("Raju")
print("after adding Raju:", friends)
# # most important friend
important_friend=input("Billa")
#replace element at index 1 with Billa
friends[1]="Billa"
# #Final list
print("Final list :",friends)


#Question2. create a list of 10 number and print the list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

#Question3.

list=[1,10,100,3,6,8]
list.insert(2,59)
list.append(5)
print("list:",list)
print("length of list:",len(list))

#Question4
words=["mobile","app","data","network","IT",]
short_words= [word for word in words if len(word)<4]
print(short_words)

# #Question5
numbers=range(20)
result=["even" if i %2==0 else "odd" for i in numbers]
print(result)

#Question6
divisible_by_7 =[i for i in range (1,1000) if i%7==0]
print(divisible_by_7)

#Question7
text="python is easy to learn"
space=text.count(" ")
print("number of spaces:", space )

#Question8
list_a=[1,2,3,4]
list_b=[2,3,4,5]
common=[num for num in list_a if num in list_b]
print(common)


