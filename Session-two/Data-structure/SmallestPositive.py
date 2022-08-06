def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    return 0
# Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2
print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

######################################################
# Solution One:
###############
def smallest_positive_a(list):
   curr_smallest = list[0]
   for i in list:
       if i < curr_smallest:
            curr_smallest = i
   return curr_smallest

######################################################
# Solution Two:
###############
def create_positive_list(list):
    return [element for element in list if element > 0]

def smallest_positive_b(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    
    positive_list = create_positive_list(in_list)
    print(positive_list)

    if len(positive_list) == 0:
        return None

    curr_smallest = positive_list[0]

    for element in positive_list:
        if element  < curr_smallest:
            curr_smallest = element
        
    return curr_smallest
######################################################
# Solution Three:
#################
def smallest_positive_c(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.

    curr_smallest = -1

    for element in in_list:
        
        if (element > 0):
            if curr_smallest == -1:
                curr_smallest = element
            if element  < curr_smallest:
                curr_smallest = element
        
    return curr_smallest

######################################################
# Solution Four:
#################
def smallest_positive_d(in_list):
    return (min([i for i in in_list if i > 0]))