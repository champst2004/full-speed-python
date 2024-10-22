def oldestStudent(ages):
  
  value = list(ages.values())
  key = list(ages.keys())
  return key[value.index(max(value))]

def updateAges(ages, n):
  new_ages = {}
  for word in ages:
    new_ages[word] = ages[word] + n
  return new_ages

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
print(oldestStudent(ages))
print(updateAges(ages, 3))