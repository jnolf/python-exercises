#a.
lm = 3
bb = 5
h = 1
p = 3
total_price = (lm*p)+(bb*p)+(h*p)
print(f'Total spent on kids movies is {total_price}')


#b.
G = 400
A = 380
F = 350
Fh = 10
Gh = 6
Ah = 4
total_pay = (Fh*F) + (Gh*G) + (Ah*A)
print (f'Total pay is {total_pay}')

#c.
Class_has_seats = True
Schedule_available = True

enroll = Class_has_seats and Schedule_available
print (f'It is {enroll} that you can enroll in class')

#d.
premium_member = True
buying_more_than_two = False
offer_not_expired = True
valid = offer_not_expired and (premium_member or buying_more_than_two)
print (f'Is this code valid? {valid}')

#e.
username = 'codeup'
password = 'notastrongpassword'

username_is_short_enough = len(username) <= 20
password_is_long_enough = len(password) >= 5
u_and_pw_different = username != password
username_has_spaces = username != username.strip()
password_has_spaces = password != password.strip()

usable_login = username_is_short_enough and password_is_long_enough and u_and_pw_different and not username_has_spaces and not password_has_spaces
print (f'Username and password are both usable? {usable_login}')


