# name = input('What is your name? ')
# favorite_color = input('What is your favorite color? ')
# print(name + ' likes ' + favorite_color)

# weight = input("Your weight (pounds)? ")
# print(type(weight))
# print(0.45359237 * float(weight))

# coures = "Jeniffer"
# another = coures[1:-1]
# print(another)

# first = "Simon"
# last = "Luong"
# msg = f'{first} [{last}] is a coder'
# print(msg)

# course = 'Python for Beginners'
# print(f'length: {len(course)}')
# print(course.find('Be'))
# print(course.title())
# print('Python' in course)

# import math
# print(math.floor(2.4))

# price = 1000000
# is_good_credit = True
# if is_good_credit:
#     price *= 0.1
# else:
#     price *= 0.2
#
# print(f'Down payment: ${price}')

# name = 'asdasdasdasdasdasdasd123123124wetfsfsdfsdfsdfsasdasdasdasdasdasdasd123123124wetfsfsdfsdfsdfs'
# if(len(name) < 3):
#     print('name must be at least 3 characters')
# elif (len(name) > 50):
#     print('name can be a maximum of 50 characters')
# else:
#     print('name looks good')

# weight = input('Weight: ')
# type_convert = input("(L)bs or (K)g: ")
# if type_convert.lower() == 'l':
#     print(f'You are {float(weight) * 0.45} kg')
# else:
#     print(f'You are {float(weight) * 2.2} pounds')

# count = 0
# # while count < 3:
# #     input_from_guess = input("Guess: ")
# #     if float(input_from_guess) == 9:
# #         break
# #     count += 1
# # if count >= 3:
# #     print("You lose")
# # else:
# #     print("You win")

command = ''
while command.lower() != 'quit':
    command = input("> ").lower()
    if command == 'start':
        print('Car started...Ready to go!')
    elif command == 'stop':
        print('Car stopped.')
    elif command == 'help':
        print('''
            start - to start the car
            stop - to stop the car
            quit - to exit
                  ''')
    elif command == 'quit':
        break
    else:
        print('I dont understand that...')
