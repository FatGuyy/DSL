# Assignmennt 3: write a python program to compute following oprerations on string:
 
# 1. To display word with the longest length
def display_largest_word(word_list):
    largest_word = ' '
    for word in word_list:
        print(word, len(word))

words = input("Enter your string :")
word_list = words.split()
display_largest_word(word_list)

# 2. To determine frequncy of occurence of a particula character in the string
s= input("Enter some string: ")
frequency_dict = { }
for character in s :
    if character in frequency_dict:
        frequency_dict[character] += 1
    else:
        frequency_dict[character] = 1
print("--------------------------------------------------------------------------")        
print("Character\tFrequency")
print("--------------------------------------------------------------------------")
for character, frequency in frequency_dict.items() :
    print("%5c\t\t%5d" %(character, frequency))   

# 3. To check wheather given string is palindrome or not  
string = input("Enter your string:")
if(string == string[::-1]):
    print("This is a palindrome")
else:
    print("This is not a palindrome")

# 4. To display index of first appearance of the substring
s = input("Enter your string : ")
substring =input("Enter substring : ")

index = s.find(substring)
print(index) 

# 5. To count occurencess of each word
s = input("Enter string :" )
word = input("Enter word :")
a = []
count = 0
a = s.split(" ")
for i in range (0, len(a)) :
    if word == a[i]:
        count = count + 1
    print("Count of the word is : ")    
    print(count)
