dict = {('Lexus',2015):5.1,('Lexus',2016):5.2,('Toyota',2015):4.1,('Toyota',2016):4.2}
x = dict.get(('Lexus',2016))
print(x)
y = dict.get(('Toyota',2014))
print(y)
z = ('Toyota',2015) in dict
print(z)
dict[('Toyota',2014)] = 4.0
print(dict)
print(dict.pop(('Toyota',2016)))
print(dict)
del dict[('Toyota',2014)]
print(dict)
for key, value in dict.items():
  print(key,"=",value)


to_remove = []
# cant for i in dict:
  # dict.pop(i)
for i in dict:
  if(i[1] > 2015):
    to_remove.append(i)
for i in to_remove:
  dict.pop(i)
print(dict)