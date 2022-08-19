x=input('Enter a string: ')
print(x.upper())

print(x.capitalize())

list_1=x.split()
list_1.reverse()
for i in list_1:
    print(i,end=' ')
print('')
    
for i in range(list_1.__len__()):
    if i%2 !=0:
        print(list_1[i],end=" ") 