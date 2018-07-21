'''This file prints to list
    1) List of numbers > N
    2) List of numbers <= N
'''

list_all =input('Give the list you want to divide\n')
N = int(input('Type the pivot\n'))

#covert list of strings to int
list_all = [int(x) for x in list_all.split()]

list_gt = [x for x in list_all if x > N]
list_lt = [x for x in list_all if x <= N]

print('Given List:\n%r\n' % list_all)
print('List with numbers greater than %r\n%r' %(N, list_gt))
print('List with numbers less than or equal to %r\n%r' %(N, list_lt))



