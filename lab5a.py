#!/usr/bin/env python3

#Author ID: mcini

def read_file_string(file_name):
    f =open(file_name, 'r')
    file_string = f.read()
    f.close()
    return file_string
def read_file_list(file_name):
    f = open(file_name)
    list1 = f.read().strip().split('\n')
    f.close()
    return list1

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
