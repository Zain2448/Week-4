"""

for i in range(0,11,2):
    print(i)

list = ["a","b","c","b"]
for letter in list:
    print (letter)

if "e" not in list:
    print("E is not found")

# the debugger executes one line at a time and it stops at the line with the error
# do while guarantees the loop is execute once, whereas a while loop maybe false from the start
# this can be compensated by the keyword break

while True:
    username = input("Enter a Username: ")
    if username == "zain":
        print("Username is correct")
        break
    else:
        username = input("Enter a Valid Username:")

numberlist = [1,2,3,4,5,6,7,8,9,10]
print(max(numberlist))
print(min(numberlist))
"""
password = input("Enter a password")
length = False
upper = False
lower = False
digit = False
special = False
check = False
if len(password) < 12 and len(password) > 8:
    length = True

print(length)
for i in password:


    if password.isupper() == False:

    if password.islower() == False:

    if password.isdigit() == False:



