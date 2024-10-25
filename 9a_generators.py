'''
A Python generator is a convenient way to implement an iterator. Instead of a class,
a generator is a function which returns a value each time the yield keyword is used. 
Here's an example of a generator to count the values between two numbers
'''

def myrange(a, b):
  while a < b:
    yield a
    a += 1
a = myrange(2, 4) # call the generator function which returns an object
print (next(a)) # iterate through items using next
print (next(a))
#print (next(a)) error as range is defined from 2-4

print("-----")
for value in myrange(1, 4):
  print(value)
print("-----")


'''
The interesting thing about generators is the yield keyword. 
The yield keyword works much like the return keyword, but—unlike return—it allows the 
function to eventually resume its execution. In other words, each time the next value of a generator is needed, 
Python wakes up the function and resumes its execution from the yield line as if the function had never exited.
'''

def squares(n):
  for value in range(n):
    yield value * value

sqr = squares(8)
print(next(sqr))
print(next(sqr))
print(next(sqr))
print(next(sqr))
print(next(sqr))
print(next(sqr))