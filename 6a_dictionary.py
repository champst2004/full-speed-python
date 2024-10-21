ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

print("Get age of all persons")
for key, value in ages.items(): 
    print(key, value) 

print(ages.keys())
print(ages.values())

for x in ages:
  print(x)

for x in ages:
  print(ages[x])