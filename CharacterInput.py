# Character Input
# Program that asks user for name and age. Prints out message that tells them when they will turn 100 years old 

import datetime
import re

def main():
    userInput = input("Enter name, followed by age: ") 
    m = re.search('([^\d]*)(\d+)',userInput)
    print(m.group(1).rstrip())
    current = datetime.datetime.now()
    print(m.group(1),'will turn 100 in the year', (int(current.year) + (100 - int(m.group(2)))))


main()