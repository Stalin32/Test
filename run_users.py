import users

user = users.Admin('ivan', 'ivanov', 'male', 23)

user.privileges.show_privileges()
user.greet_user()