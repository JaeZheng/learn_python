from User import User, Admin, Privileges

admin = Admin("Koe", "Elan", "12")
admin.describe_user()
admin.privileges.show_privileges()