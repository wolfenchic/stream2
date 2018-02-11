#This test checks for an even number of even numbers. 
from byot import *

def add_to_list(l, item):
    l.append(item)

names = ["Richard", "Katie", "Stephen", "Dan"]
add_to_list(names, "Arne")

test_in_collection(names, "Arne")

def even_number_of_evens(l):
    evens= len([i for i in l if i % 2== 0])
    return evens %2 == 0
       
test_are_equal(even_number_of_evens([]), True)       
test_are_equal(even_number_of_evens([2, 5]), False) 
test_are_equal(even_number_of_evens([4, 8, 1]), True)     
test_are_equal(even_number_of_evens([12, 8, 14, 2]), True) 
test_are_equal(even_number_of_evens([12, 8, 14]), False) 
test_are_equal(even_number_of_evens([1, 13, 5, 9]), True) 
test_are_equal(even_number_of_evens([1, 13, 5]), True) 
test_are_equal(even_number_of_evens([-2, -4]), True) 
test_are_equal(even_number_of_evens([0, 2]), True) 

#assert even_number_of_evens([]) == True, "Empty List"
#assert even_number_of_evens([2, 5]) == False, "One even number"
#assert even_number_of_evens([4, 8, 1]) == True, "Two even numbers and one odd number"
#assert even_number_of_evens([12, 8, 14, 2]) == True,"An even numbers of even numbers"
#assert even_number_of_evens([12, 8, 14]) == False, "Four even numbers not three"
#assert even_number_of_evens([1, 13, 5, 9]) == True, "There are no even numbers"
#assert even_number_of_evens([1, 13, 5]) == True, "There are no even numbers"
#assert even_number_of_evens([-2, -4]) == True, "An even number of even numbers"
#assert even_number_of_evens([0, 2]) == True, "An even number of even numbers"
print("All tests pass")
   

#print(even_number_of_evens([2, 4, 6, 9, 7, 4]))