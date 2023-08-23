#8. Write a Python program to reverse a tuples by using row code.
tuplex= (10,20,30,40,50)
rev = []
for i in range(len(tuplex)-1, -1, -1 ):
    rev.append(tuplex[i])
print(tuple(rev))