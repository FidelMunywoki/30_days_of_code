# have common type data
# union() 
# makes unique objects
""" Creating and Combining Sets of Friends """




college = set(['Bill', 'Katy', 'Verne', 'Dillon',
               'Bruce', 'Olivia', 'Richard', 'Jim'])

coworker = set(['Aaron', 'Bill', 'Brandon', 'David',
                'Frank', 'Connie', 'Kyle', 'Olivia'])

family = set(['Garry', 'Landon', 'Larry', 'Mark',
              'Olivia', 'Katy', 'Rae', 'Tom'])

friends = college.union(coworker, family)
print(friends)


# .difference() removes common items
# .symme

# set of people who live in my zip code
zipcode = set(['Jerry', 'Elaine', 'Cindy', 'Verne',
                'Rudolph', 'Bill', 'Olivia', 'Jim',
                'Lindsay', 'Rae', 'Mark', 'Kramer',
                'Landon', 'Newman', 'George'])

# .intersection() returns common elements

local = friends.intersection(zipcode)
print(local)

# # set of people who play Munchkin
munchkins = set(['Steve', 'Jackson', 'Frank', 'Bill',
                 'Mark', 'Landon', 'Rae'])

#remove the common ele munchikin and local

invite = local.difference(munchkins)
print(invite, len(invite))

# .symmetric_difference -- find common items and remove them

# set of Olivia's friends
olivia = set(['Jim', 'Amanda', 'Verne', 'Nestor'])

final_invite = invite.symmetric_difference(olivia)
print(final_invite)


print('Verne' in final_invite)
final_invite.add('Verne')
print(final_invite)