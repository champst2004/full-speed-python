def getStr(s):
  s=s[:1] + s[0] + s[1:]
  s=s[:1] + s[0] + s[1:]
  s=s[:3] + s[3] + s[3:]
  s=s[:3] + s[3] + s[3:]
  s=s[:6] + s[6] + s[6:]
  s=s[:6] + s[6] + s[6:]
  strlen = len(s)
  return [s, strlen]

print(getStr("abc"))
print(getStr("xyz"))

string = "aabbCc"
print(string.find("a"))
print(string.find("bb"))


print(string.upper())
print(string.lower())