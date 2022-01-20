# 1a. Prompt the user for the day of the week, print out 
#    whether it is monday or not.

what_is_today = input('What is today?\n')

if what_is_today.lower() != 'Monday':
    print ('Thank god it is NOT Monday!')
else:
    print ('Yep... It\'s FRICKIN\' Monday!')


# 1b. Prompt the user for the day of the week, 
#    print out whether it is a weekday or not.
 
what_is_today = input("What day is today?")

if what_is_today.lower().startswith('s'):
    print('Its the weekend!!! Yaaaay!')
else:
    print('Ugh. Not yet.')


# 1c. Calculate a weekly paycheck amount with 
#    overtime, if need be.

hours_worked = 40
hourly_rate = 28.79
weekly_pay = hours_worked * hourly_rate

if hours_worked <= 40:
    paycheck = hours_worked * hourly_rate
else:
    OT_hours = hours_worked - 40
    OT_pay = OT_hours * 1.5 * hourly_rate
    base_pay = 40 * hourly_rate
    paycheck = base_pay + OT_paymn



# 2a. Create an integer variable i with a value of 5.

# 5 to 15 by 1
i = 5 
while i < 16:
    print (i)
    i += 1


# 0 to 100 by 2
i = 0
while i < 101:
    print (i)
    i += 2


# 100 to -10 by 5
i = 100
while i >= -10:
    print (i)
    i -= 5


# 2 to 1,000,000 by **2
i = 2
while i < 1000000:
    print (i)
    i = i ** 2

# Create a loop for given output.
i = 100
while i >= 5:
    print(i)
    i -=5



# 2b.

# i.

num = input('Choose a whole number')
num = 7
for i in range(1, 11):
    print(f'{num} X {i} = {int(num) * n}')



# Create a for loop that uses print 
#  to create the output shown.
n = 1
for i in range(1, 10):
    print(str(i) * n)
    n += 1


# 2c.

while True:
    pos_num = input('Please insert an odd number betwen 1 and 50: ')
    if pos_num.isdigit():
        if int(pos_num)% 2 == 1 and int(pos_num) <= 50:
            break
pos_num = int(pos_um)
for num in range(1, 50, 2):
    if num == pos_num:
        print('Yikes! Skipping Number: ', num)
    else:
        print('Here is a odd number: ', num)


#3 FizzBuzz
#    Print the numbers from 1 to 100.
#    Multiples of 3, print "Fizz"
#    Multiples of 5, print "Buzz".
#    Multiples of both 3 AND 5, print "FizzBuzz."

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)



#4

