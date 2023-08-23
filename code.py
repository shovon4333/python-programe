#8. Write a Python program to reverse a tuples by using row code.
# tuplex= (10,20,30,40,50)
# rev = []
# for i in range(len(tuplex)-1, -1, -1 ):
#     rev.append(tuplex[i])
# print(tuple(rev))

# 7. Write a Python program to unzip a list of tuples into individual lists
l=[(1,2), (3,4), (8,9)]
list1=[]
list2=[]
for tuplex in l:
    list1.append(tuplex[0])
    list2.append(tuplex[1])
print(tuple(list1), end=" ")
print(tuple(list2))