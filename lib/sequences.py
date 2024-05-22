#!/usr/bin/env python3

def print_fibonacci(n):
    if n <= 0:
        print([])
        return 
    
    list = [0,1]
    while len(list) < n:
        new_list = list[-1] + list[-2]
        list.append(new_list)

print(list())
    