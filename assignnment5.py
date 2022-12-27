# Assignment 5: Gaurav Sonawane B47
n = int(input("Enter how many names you want to enter: "))
# initialize empty dictionary
names={}
for i in range(n):
    name=input("Enter name of friend: ")
    number=input("Enter phone number: ")
    names[name]=number #add name number to dictionary
print(names)
names["Arun"]="9877666234" #add new item
print("Modified dictionary ",names)
del names["Arun"] #delete an item
for name in names: #modify first key value
    names[name] = "9456356344"
    break
print("Amit" in names)
print("dictionary in sorted order")
for i in sorted (names) : #sort the dictionary
    print((i, names[i]), end =" ")

    