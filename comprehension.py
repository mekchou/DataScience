list1 = [i**2 for i in range (1,11)]
print(list1)

import random
list2 = [random.randint(0,5) for i in range (0,10)]
print(list2)

dict1 = {i:i**2 for i in range (1,11)}
print(dict1)

dict2 = {i:chr(i) for i in range (65,90)}
# dict2.  {[i:chr(i) for i in range (97,122)]}
print(dict2)