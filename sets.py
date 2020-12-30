color_1 = set(['red','blue','yellow'])
print(color_1)
color_1.add('green')
print(color_1)
color_1.update(['white','black'])
print(color_1)
color_1.discard('white')
print(color_1)
color_1.difference_update(['white','black'])
print(color_1)

color_2 = set(['red','green','blue'])
print(color_2)

either = color_1.union(color_2)
print(either)

both = color_1.intersection(color_2)
print(both)
both