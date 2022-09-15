import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333',
             'Joe':'555-4444'}



print()
print('*****  start section 1 - print dictionary ********')
print()





print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()







print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()





print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()




print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()






print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()






print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

# a = phonebook.pop('Chris', 'not found')

# print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()

# print(phonebook)
# a = phonebook.popitem()
# print(a)
# print(phonebook)




print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)
random_key = random.choice(list_of_keys)
print(random_key)
random_value = phonebook[random_key]
print(random_value)


#alternatively
random_value = phonebook[random.choice(list(phonebook))]
print(random_value)

print()
print('*****  end section 9 ********')
print()