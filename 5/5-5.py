def get_point(color):
    if color == 'green':
        print("get 5 point.")
    elif color == 'yellow':
        print("get 10 point.")
    else:
        print("get 15 point.")


alien_color = 'green'
get_point(alien_color)
alien_color = 'yellow'
get_point(alien_color)
alien_color = 'red'
get_point(alien_color)