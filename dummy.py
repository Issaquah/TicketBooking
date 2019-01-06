lst = []

size_of_list = int(input("Enter the size of list:"))

for i in range(size_of_list):
    inp = input("Enter the element:")
    lst.append(inp)

res = dict((i, lst.count(i)) for i in lst)
print(res)

lst.append(res)
for i in lst[:3]:
    print(lst)

