#set
'''alpha={'a', 'b', 'c', 'd', 'e'}
print(alpha)
print(len(alpha))'''
'''for i in alpha:
    print(i)'''

'''alpha.add('f')
alpha.update(['g', 'h', 'i'])
alpha.pop()
alpha.remove('a')
alpha.clear()
del alpha'''
'''print(alpha)

if 'a' in alpha:
    print("Yes")
else:
    print("No")'''

data=set()
n=int(input("Enter number of elements:"))

for i in range(n):
    x=input("Enter city:")
    data.add(x)

print(data)