#!/usr/bin/env python3

# Author ID: mcini

def add(number1,number2):
    try: 
        total = int(number1) + int(number2)
        return total
    except (TypeError, ValueError):
        message = 'error: could not add numbers'
        return message
def read_file(filename):
    try:
        f = open(filename,'r')
        list1 = list(f)
        return list1
    except FileNotFoundError:
        message = 'error: could not read file'
        return message
if __name__ == '__main__':
    print(add(10,5))                        
    print(add('10',5))                      
    print(add('abc',5))                     
    print(read_file('seneca2.txt'))         
    print(read_file('file10000.txt'))       