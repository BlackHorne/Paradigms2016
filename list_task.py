# Remove equal adjacent elements
#
# Example input: [1, 2, 2, 3]
# Example output: [1, 2, 3]
def remove_adjacent(lst):
    lst1 = []
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
           lst1.append(lst[i]) 
    lst1.append(lst[len(lst) - 1])
    return lst1

# Merge two sorted lists in one sorted list in linear time
#
# Example input: [2, 4, 6], [1, 3, 5]
# Example output: [1, 2, 3, 4, 5, 6]
def linear_merge(lst1, lst2):
    answ = []
    dl1 = len(lst1)
    dl2 = len(lst2)
    ng1 = ng2 = 0
    while ng1 < dl1 and ng2 < dl2:
        if lst1[ng1] > lst2[ng2]:
            answ.append(lst2[ng2])
            ng2 += 1
        else:
            if lst1[ng1] <= lst2[ng2]:
                answ.append(lst1[ng1])
                ng1 += 1
    if ng1 == dl1:
        while ng2 < dl2:
            answ.append(lst2[ng2])
            ng2 += 1
    else:
        while ng1 < dl1:
            answ.append(lst1[ng1])
            ng1 += 1
    return answ


