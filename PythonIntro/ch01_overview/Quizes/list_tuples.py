# Edit and run this script to perform the following. Modified this to work with functions for practice

records = [
    ('John', 'Smith', 43, 'johns@example.com'),
    ('Ellen', 'James', 22, 'steves@example.com'),
    ('Sally', 'Edward', 21, 'se@example.com'),
    ('Keith', 'Cramer', 12, 'otienos@example.com'),
    ('Brozy', 'T', 29, 'otienos@example.com')
]


# step1. Display users age
def display_users_age():
    # ask for user firstname
    first_name = input('Please enter Fist Name: ')
    last_name = input('Please enter Last Name: ')
    # loop through the user tuples and if username matches display the age
    for tup in records:
        if first_name in tup[0] and last_name in tup[1]:
            print(f'{first_name} {last_name} is {tup[2]} years old')


display_users_age()


# step2. Add user
def add_user(records):
    # get user info
    first_name = input('Please enter Fist Name: ')
    last_name = input('Please enter Last Name: ')
    age = input('Please enter age: ')
    email = input('Please enter email: ')

    # join the info and place it in a tuple
    new_user = tuple(' '.join((first_name, last_name, age, email)).split())
    # add new user to records
    print('Adding new user to db')
    records.append(new_user)


add_user(records)


# step3 display all the records
def diplay_records(records):
    print('Displaying records...')
    for user in records:
        first_name, last_name, age, email = user
        # print(f'{first_name} {last_name} {age} {email}')
        print('{0:10}{1:10}{2:10}{3:100}'.format(first_name, last_name, age, email))  # using format


diplay_records(records)
