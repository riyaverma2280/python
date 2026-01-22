#QUESTION1 the guest list
Friday={"Alice","Bob","Charlie"}
Saturday={"Charlie","David","Eve"}
#guest attending at least one night(union)
all_guest=Friday | Saturday    #union(|) combines both sets without duplicates
#guest attending both nights(intersection)
both_night=Friday & Saturday     #intersection(&) finds common element in both sets
print("all_guest:", all_guest)
print("guest attending both night:",both_night)

#QUESTION2.   LIST CLEANER
data=[1,2,2,3,4,4,4,5]
clean_list=list(set(data))    # remove duplicate values
clean_list.append(6)
print(clean_list)

#QUESTION3. LIBRARY AUDIT
library_books = {"Hobbit", "1984", "Gatsby", "Odyssey", "Hamlet"}
checked_out = {"1984", "Hamlet"}
available_books = library_books - checked_out   # use set differnce(-)
print("Available books:", available_books)

new_book = "Don Quixote"

if new_book not in library_books:
    library_books.add(new_book)
    print(f'"{new_book}" added to the library.')
else:
    print(f'"{new_book}" is already in the library.')

print("Updated library:", library_books)

#QUESTION4'
def check_permissions(user_permissions, admin_reqs):
    # Check if user has all admin permissions
    if admin_reqs.issubset(user_permissions):
        print("User has admin access")
    else:
        print("User does NOT have admin access")

 # Find missing permissions
        missing = admin_reqs - user_permissions
        print("Missing permissions:", missing)
# Given sets
user_permissions = {"read", "write"}
admin_reqs = {"read", "write", "execute"}

# Function call
check_permissions(user_permissions, admin_reqs)

#QUESTION5.
logs = {
    "404": [10, 12, 15, 20],
    "500": [12, 20, 22, 25],
    "403": [10, 20, 30]
}
#task1.
common_servers = {
    server
    for server in logs["404"]
    if server in logs["500"] and server in logs["403"]
}

print(common_servers)

#task2.
critical_servers = {
    server
    for server in logs["500"]
    if server not in logs["404"]
}

print(critical_servers)

