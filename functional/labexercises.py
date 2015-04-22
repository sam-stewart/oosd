# Lambda expression exercises (lab 8.1)

# Computes factorials
reduce(lambda x, y : x * y, range(1, 6))

# Function takes a string, and a char, returns new string without chars.
remove_char = lambda c, st : filter(lambda x : x != c, st)
remove_char('c', 'christchurch')

# Returns occurences of char in string
len(filter(lambda x : x != 'c', 'christchurch'))
reduce(lambda x, y: x + 1 if y == 'c' else x + 0, 'christchurch', 0)

# Take string and char, return the number of words starting with char
st = """Never drive Vin Diesel's car. Vin Diesel's car has twenty-six gears. 
    It is much too difficult"""
c = 'c'

def count_words(c, st):
    return len(filter(lambda x : x.startswith(c), st.split()))
print str(count_words(c, st))

# Take string and char, returns new string with all occurences of char uppercase.
# This is retarded, st.replace is all that is needed.
#to_upper = lambda c, st : st.replace(c, c.upper)
#print to_upper(c, st)

# Version of map() using a loop
def mymap(f):
    retlist = []
    for i in range(1,10):
        retlist.append(f(i))
    return retlist

print mymap(lambda x : x * 2)

# Version of map() using recursion
def mymapr(l, retlist = []):
    retlist.append(2 * l.pop())
    if len(l) > 0:
        mymapr(l, retlist)
    return retlist
print(mymapr(range(1,10)))



    
    


