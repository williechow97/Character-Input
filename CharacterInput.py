# Character Input
# Program that asks user for name and age. Prints out message that tells them when they will turn 100 years old 

import datetime

def main():
    userInput = input("Enter name, followed by age: ") 
    (name, age) = userInput.split(' ')
    #print( name)
    current = datetime.datetime.now()
    #print(current.year)
    print(name,'will turn 100 in the year', (int(current.year) + 100))
main()