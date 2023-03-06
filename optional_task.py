#Ask user to input their favourite restaurant and store it in a variable called fav_rest
#Ask user to input their favourite number and store it as integer in a variable called int_fav
#Print both separately
#Error returns casting fav_rest into an integer because it consist of characters and not integers

fav_rest = input("Enter the name of your favourite restaurant: ")
int_fav = int(input("Enter your favourite number: "))
print(fav_rest)
print(int_fav)
print(int(fav_rest))