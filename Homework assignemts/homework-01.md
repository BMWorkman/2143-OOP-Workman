'''python
"""
name: Brett Workman
email: brettworkman2014@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 31 jan @ 11:00 a.m.
"""


A.) What would Python print?
    a = [1, 5, 4, 2, 3] 
    print(a[0], a[-1])
    # Prints: 1 3

    a[4] = a[2] + a[-2]
    Print(a)
    # Prints: [1, 5, 4, 2, 6]

    print(len(a))
    # Prints: 5

    print(4 in a)
    # Prints: true

    a[1] = [a[1], a[0]]
    print(a)
    # Prints: [1, [5, 1], 4, 2, 6]
    
B.) Write a function that removes all instances of an element from a list.
    def remove_all(el, list):

C.) Write a function that takes in two values, x and y, and a list, and adds as many y's to the end of the list as there are x's. Do not use the built-in function count.
    add_this_many(x, y, list):

D.) What would Python print?
    a = [3, 1, 4, 2, 5, 3]
    print(a[:4])
    # Prints: [3, 1, 4, 2] because it says print out the first four numbers
    # of the array

    print(a)
    # Prints: [3, 1, 4, 2, 5, 3] 

    print(a[1::2])
    # Prints: [1, 2, 3]
    # it prints out the array but only every other number starting after the
    # irst number

    print(a[:])
    # Prints: [3, 1, 4, 2, 5, 3]

    print(a[4:2])
    # Prints: []
    # it just prints out nothing bcause you are saying "print out the numbers in
    # chronological order from 4 - 2" 

    print(a[1:-2])
    # Prints: [1, 4, 2]

    print(a[::-1])
    # Prints: [3, 5, 2, 4, 1, 3]
    # it just prints it out in reverse order

E.) Let's reverse Python lists in place, meaning mutate the passed in list itself, instead of returning a new list. We didn't discuss this in class directly, so feel free to use google. Why is the "in place" solution prefered?
    def reverse(list):
    # in place is prefered because instead of just reversing the numbers and placing 
    # them in new locations it simply reverses the locations of the numbers.


F.) Write a function that rotates the elements of a list to the right by k. Elements should not ”fall off”; they should wrap around the beginning of the list. rotate should return a new list. To make a list of n 0's,you can do this: [0] * n
    def rotate(list, k):


(no G..... i guess?) 

    superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}
print(superbowls['tom brady'])
# Prints: 3

superbowls['peyton manning'] = 1
print(superbowls)
# Prints: {'peyton manning': 1, 'tom brady': 3, 'joe flacco': 0, 'joe montana': 4}

superbowls['joe flacco'] = 1
print(superbowls)
# Prints:{'peyton manning': 1, 'tom brady': 3, 'joe flacco': 1, 'joe montana': 4}

H.) Continuing from above, what would Python print?
    print('colin kaepernick' in superbowls)
    #Prints: False (because Colin Kaepernick isnt there)

    print(len(superbowls))
    #Prints: 4 (because that is the length of the dictionary)

    print(superbowls['peyton manning'] == superbowls['joe montana'])
    #Prints: False (because peyton manning is defined as 1 while joe is
    # defined as 4 and 1 =/= 4

    superbowls[('eli manning', 'giants')] = 2
    print(superbowls)
    #Prints: {'joe montana': 4, ('eli manning', 'giants'): 2, 'tom brady': 3, 'peyton manning': 1, 'joe flacco': 1}

    superbowls[3] = 'cat'
    print(superbowls)
    #Prints: {'joe montana': 4, ('eli manning', 'giants'): 2, 3 : 'cat', 'tom brady': 3, 'peyton manning': 1, 'joe flacco': 1}


    superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
    print(superbowls)
    # print: {('eli manning', 'giants'): 5, 3: 'cat', 'tom brady': 3, 'peyton manning': 1, 'joe flacco': 1, 'joe montana': 4}

    superbowls[['steelers', '49ers']] = 11
    print(superbowls)
    #Prints: it will give us an error code. however, superbowls[('steelers', '49ers')] = 11
    # will print this: {3: 'cat', 'joe flacco': 1, 'peyton manning': 1, ('eli manning', 'giants'): 5, 'tom brady': 3, ('steelers', '49ers'): 11, 'joe montana': 4}

I.)Given a dictionary replace all occurrences of x as the value with y.
    def replace_all(d, x, y):
J.) Given a (non-nested) dictionary delete all occurences of a value. You cannot delete items in a dictionary as you are iterating through it (google :) ).
    def rm(d, x):

'''
