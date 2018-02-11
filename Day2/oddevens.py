def odd_number_of_odds(l):
    new_list=[]
    for i in l:
        if not i%2==0:
             new_list.append(i)
    
    return not len(new_list)%2==0
            

assert odd_number_of_odds([]) == False, "Empty List"
assert odd_number_of_odds([2, 5]) == True, "One even number"
assert odd_number_of_odds([4, 8, 1]) == True, "Two even numbers and one odd number"
assert odd_number_of_odds([12, 8, 14, 2]) == False,"An even numbers of even numbers"
assert odd_number_of_odds([12, 8, 14]) == False, "Four even numbers not three"
assert odd_number_of_odds([1, 13, 5, 9]) == False, "There are no even numbers"
assert odd_number_of_odds([1, 13, 5]) == True, "There are no even numbers"
assert odd_number_of_odds([-2, -4]) == False, "An even number of even numbers"
assert odd_number_of_odds([0, 2]) == False, "An even number of even numbers"
print("All tests pass")
