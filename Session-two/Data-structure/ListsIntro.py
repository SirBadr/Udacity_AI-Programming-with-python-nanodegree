list_a = [1,2,3,4]
list_b = ["a", "B", "C"]


list1 = [1, 2, "Udacity", "AI"]

print(list1)
print(len(list1))
print(list1[1])
print(list1[-1])
print(list1[-3])
print(list1[1:])
print(list1[:2])
print(list1[:len(list1)])
print(list1[-3:])
## then python list is ordered

list1[1] = "nanodegree"
print(list1)
## then python list is mutable


list4 = [1,2.5,[3,4,True]]

print(list4)
print(list4[2])
print(list4[2][0])

list4[2][1] = "programming"
print(list4[2])

###########################################################################
#################### Membership operators #################################
print(1 in list1)
print(1 not in list1)
print([3, 'programming', True] in list4)