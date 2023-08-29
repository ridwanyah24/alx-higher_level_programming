#!/usr/bin/python3
def insert_in_list(key, value, the_list=[]):
    the_list.append([{f'{key} : {value}'}])
    for i in the_list:
    	print(i)

test_list = []
insert_in_list('Name', 'Ridwan', test_list)
    
    
	
