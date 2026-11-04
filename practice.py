names = [ 'sara', 'jenna', 'kareyle','mishal', 'ishmal']
print(names[2]) # this is for acsessing any element from list
print(names[-2])# this is use to acsess element from last side of list

proffession = 'Ai Engineer'
print(list(proffession))# this is use to access each character in list even space

length = ['sara', 'jenna', 'kareyle']
print(len(length))

ages = [10,20,17,18,29,30,50,49]
ages[2] = 16# here i changed element at specific index like on[2] it was 17 but now its 16
ages[-2] = 60
print(ages)


movies = ['suspense','thriller','horror','comedy']
del movies[2]
print(movies)#to delete an element from array

# reviews = ['bad','good','honest','badest']
# print(reviews[6])#IndexError: list index out of range

programming_languages = ['Python', 'Java', 'C++', 'Rust']
print('C++' in programming_languages)

developer = ['Alice', 25, ['Python', 'Rust', 'C++']]#to get index of nested items inarray
print(developer[2][2])

developer = ['Alice', 34, 'Rust Developer']
name,age,job = developer
print(job)#unpack array by assigning each value of aaray to separate variables

developer = ['Alice', 34, 'Rust Developer']
age, *rest = developer
print(age, *rest)#to get rest of items 

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
print(desserts[1:3])#to get item from array where it starts and where before it ends

numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1:6:3])#start at index 1  stop at index 6  and move 1 index further

#List Methods

numbers = [1, 2, 3, 4, 5]
numbers.append(6)#use to add elements in end of array
numbers.extend([4,8,7,4])#to add multiple items
print(numbers)

numbers = [1, 2, 3, 4, 5,6,8]
even_numbers = [2,4,6,8]
numbers.append(even_numbers)
print(numbers)

numbers = [1, 2, 3, 4, 5,6,8,9]
# odd_numbers = [3,5,7,9,11]
numbers.insert(3,3.5)#insert item at specific index
print(numbers)

odd_numbers = [3,5,7,9,9,11]
odd_numbers.remove(9)#remove first occurance of item
print(odd_numbers)

odd_numbers = [3,5,7,9,11,11]
odd_numbers.pop(4)#remove item at specific index
print(odd_numbers)

whole_numbers = [10,20,30,40,50,60]
whole_numbers.clear()
print(whole_numbers)

whole_numbers = [40,20,40,10,50,80]
whole_numbers.sort()
print(whole_numbers)

whole_numbers = [10,20,30,40,50,60]
sorted_list = sorted(whole_numbers)
print(whole_numbers)
print(sorted_list)

whole_numbers = [10,20,30,40,50,60]
whole_numbers.reverse()
print(whole_numbers)

programming_languages = ['Rust', 'Java', 'Python', 'C++']
print(programming_languages.index('Python'))

#Tuples are group of data and are unchangeable
# programming_languages = ('Python', 'Java', 'C++', 'Rust')
# programming_languages[0] = 'JavaScript'

food = 'biryani'
print(tuple(food))
print('r' in food)

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)

    developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")

        languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

    languages = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages)))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]



categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)#for nested arrays

#range(start, stop, step)
for num in range(2, 11, 2):
    print(num)

for num in range(40, 0, -10):
    print(num)


