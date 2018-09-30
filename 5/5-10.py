current_users = ["admin", "Jae", "Kobe", "Alan", "Fri"]
new_users = ["admin", "Jae", "Helen", "May", "ALAN"]
for user in new_users:
    if user.title() in current_users:
        print(user + " is in current_users.")
    else:
        print(user + " add success.")