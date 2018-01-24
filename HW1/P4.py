
# my favorite universities
mine = ['Yale', 'MIT', 'Berkeley']
# your favorite universities
yours = ['Caltech', 'Harvard', 'Duke']

# our favorite universities
ours1 = mine + yours
print('ours1 (list of our favorite universities built using the + operator):\n', ours1)

# our favorite universities
ours2 = []
ours2.append(mine)
ours2.append(yours)
print('ours2 (list of our favorite universities built using the append operator):\n', ours2)

# change your second favorite school from 'Harvard' to 'Yale
yours[1] = 'Yale'
print('The new list of your favorite universities:\n', yours)

# print the new lists of our favorite classes
print('ours1: will remain the same as before:\n', ours1)
print('ours2: will change:\n',ours2)


# When we use + operators, the values of lists 'mine' and 'yours' are being copied into a new list 'ours1'.
# On the other hand, when we use .append() to create 'ours2', the references to (not the values of)
# 'mine' and 'yours' get copied into the list 'ours2'. Therefore, any change to either 'mine' or 'yours' list
# will be reflected in 'ours2'.
# Also note that the elements of ours1 are strings while the elements of ours2 are themselves lists.

