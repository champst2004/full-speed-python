def find_students(address, students):
  names = []
  for key, subdict in students.items():
       for sublist in subdict.values():
          if (sublist == address):
             names.append(key)
  return sorted(names)

def find_students1(address, students):
  names = []
  for key, value in students.items():
    if value["address"] == address:
      names.append(key)
  return sorted(names)

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
}

print(find_students("Lisbon", students))
print(find_students1("Lisbon", students))