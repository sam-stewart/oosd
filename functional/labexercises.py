# Lambda expression exercises (lab 8.1)
# File conventions: c is a character, st is a string, l is a list.

#1 Computes factorials from a list
def factorial(l):
    return reduce(lambda x, y : x * y, l)

#2 Function takes a string, and a char, returns new string without chars.
remove_char = lambda c, st : filter(lambda x : x != c, st)

#3 Returns number of occurences of char in string
def occurences(c, st):
    return len(filter(lambda x : x != c, st))

#4 Counts words in string beginning with char c.
def count_words(c, st):
    return len(filter(lambda x : x.startswith(c), st.split()))

#6 version of map() using a loop (map takes a function and a list)
def mymap_loop(f, l):
    retlist = []
    for i in l:
        retlist.append(f(i))
    return retlist

#7 Version of map() using recursion (map takes a function and a list)
def mymap_recursive(f, l):
    if not l:
        return [] 
    return [f(l[0])] + mymap_recursive(f, l[1:])

    


    
    


