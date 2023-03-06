#Get user to input a sentence
#Store value in a variable
#Calculate and print len of str
#Find the last letter of the str
#Replace last letter of the str with "@"
#Print last 3 characters of the str
#Use the first 3 and the last 2 characters to make up a word
#Split str 
#Join and print str words on separate lines

str_manip = input("Please enter a sentence: ")
print(len(str_manip))

last_character = (str_manip[-1])
repl_str = str_manip.replace(last_character, "@")
print(repl_str)

print(str_manip[ :-4:-1])
five_letter_word = str_manip[ :3] + str_manip[-2: ]
print(five_letter_word)

spl_str = str_manip.split(" ")
print(spl_str)

joint_str = "\n".join(spl_str)
print(joint_str)
