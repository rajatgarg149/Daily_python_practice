''' I'll tell user, the year when he/she will turn 100.'''

print('Hello user!')
name = input('Mention your name.\n')
age = input('Input your current age.\n')
print('\nUSER DATA :\nName - %r\nAge - %r' %(name, age))

import datetime
year = datetime.datetime.now().year
print("\n\nYou'll be 100 in year - %r!"%(year+100-int(age)))
