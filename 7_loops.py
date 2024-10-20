def hasDuplicates(list):
  res = False
  for i in range(len(list)):
    for j in range(len(list)):                  # or range(i + 1, len(list))
      if (list[j] == list[i]) and j != i:       # or (list[j] == list[i])
        res = True
  return res