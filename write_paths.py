def write_paths(text):
    with open('user_preferences.txt', 'a') as file:
        file.write(text + '\n')


# write_paths('test')