# lists.
# sets.
# Tuples.
# dictionaries.

#list_a = [1,4,3,2,0]
#list_b = [1,2,1.3,4,"stringsss"]
#list_c = [1,1.4,["string", 1,2], 5, 6, 7]
#list_d = ["hi", "i", "am", "mahmoud"]

#print("-".join(list_d))


#print(list_a)
#list_a = sorted(list_a)
#print(list_a)
#list_a[0] = 5
#print(list_a)
#print(list_b[len(list_b) - 1])
#print(list_c)


#list_a = [1,1,2,3,4,4,5]
#newSet = set(list_a)
#newSet[0] = 12
#print(newSet[0])



# tuples
#tupl = (1,2)
#tupl[0] = 2
#print(tupl)

#dictionary







def smallest_positive_a(lista):
    if(len(lista) == 0):
        return -1


    curr_smallest = lista[0]
    #for j in lista:
    #    if j > 0:
    #        curr_smallest = j

    #curr_smallest = lista[0]   #curr_smallest = -1

    for i in lista:
        if curr_smallest <= 0:
            curr_smallest = i
            continue
            
        if i < curr_smallest and i > 0:   #there will be no positive value that is smaller that curr_smallest
            curr_smallest = i 
    return curr_smallest

# if list is empty, it'll break
print(smallest_positive_a([-1,0,1,3,4,56,4]))
