def count_upper_case(message):
   count = 0
   for c in message:
       if c.isupper():
           count += 1
   return count

#message = "Hello"   
#l = [c for c in message if c.isupper()]
#print(sum(l))
   
test = ["A", "b", "c", "D", "e", "F"] 
print(test)
#sum(map(str.isupper, test))



assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case("p") == 0, "One lower case"
assert count_upper_case(test) == 3, "Three upper case"

print("All the tests passed")
