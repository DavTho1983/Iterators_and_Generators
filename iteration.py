#While loop bad example!
i = 0
my_list = ['a', 'b', 'c', 'd', 'e']
while i < len(my_list):
    v = my_list[i]
    print(v)
    i += 1
#Better but still has integers
for i in range(len(my_list)):
    v = my_list[i]
    print(v)

#Best
for v in my_list:
    print(v)

#Iterating a dict gives keys
d = { 'A' : 1,
    'B' : 2,
    'C' : 3,
    }

for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)
