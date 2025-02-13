password = input("Enter a password: ")
username = input("Enter a username: ")

# if password == 'secure123' and username == 'admin':
#     print("Login successful!")
# elif password == 'secure123':
#     print('Invalid username!')
# elif username == 'admin':
#     print('Invalid password!')
# else:
#     print('Invalid username and password!')

if password != 'secure123' and username != 'admin':
    print('Invalid username and password!')
elif password != 'secure123':
    print('Invalid password!')
elif username != 'admin':
    print('Invalid username!')
else:
    print('Login successful!')