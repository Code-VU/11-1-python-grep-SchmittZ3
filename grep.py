import re
import string
import sys


def countpatterninfile():
    regular_expression = input("Enter a regular expression: ")
    x = open('mbox-long.txt')
    count = 0

    for line in x:
        if re.search(regular_expression, line):
            count = count + 1

    print("mbox.txt had",(count),'lines that matched',(regular_expression))
    
  #  print('mbox.txt had' (z) 'lines that matched' (regular_expression))



if __name__ == '__main__':
    # this is called a main method
    # This is another way of telling python THIS IS WHERE YOU SHOULD START RUNNING
    # When this is included, python will begin with the code in this block first
    countpatterninfile()