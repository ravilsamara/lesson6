a= [99,0,35,1,6,2]
b = [1,1,2,33,5,8,13,21,34,55,89]
c= []
for i in a:
    if i in b:
        c.append(i)
print(c)
