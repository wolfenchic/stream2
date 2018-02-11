l= [1, 2, 3, 4, 5, 6]
print(sum(l))



nums = list(range(0,99))
print(nums)


nums2 = list(range(10, 52, 2))
print(nums2)

listA = [[0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6]]
print(listA[4][3])

evens = []
for x in range(1, 11):
    if x%2 == 0:
        evens.append(x)

print(evens)

fruit = ['apple', 'orange', 'plum', 'berry', 'kiwi', 'grape', 'banana', 'pineapple', 'pear', 'tomato']
print(fruit[0])
print(fruit[9])
print(fruit[1:10])
print(fruit[0:9])

students = [
    {
    'name': 'nichola',
    'age': 20,
    'nationality': 'irish', 
    'subjects': ['javascript', 'python', 'css', 'html']
},

{
    'name': 'arne',
    'age': '20',
    'nationality': 'german', 
    'subjects': ['javascript', 'python', 'css', 'html']
},

{
    'name': 'stephen',
    'age': '20',
    'nationality': 'irish', 
    'subjects': ['javascript', 'python', 'css', 'html']
},

{
    'name': 'jordan',
    'age': '20',
    'nationality': 'irish', 
    'subjects': ['javascript', 'python', 'css', 'html']
},
]

words = {
    'big': "large, not tiny",
    'small': 5,
    'car': 3,
    'student': 7
}

print(words['small'])