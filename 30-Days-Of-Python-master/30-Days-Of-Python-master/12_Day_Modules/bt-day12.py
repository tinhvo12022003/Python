            #LEVEL 1
#bài tập 1
import random 
import string

#bài tập 1
def generate_random_user_id():
    characters = string.ascii_letters + string.digits
    random_user_id = ''.join(random.choices(characters, k=6))
    return random_user_id

#bài tập 2
def user_id_gen_by_user():
    num_users, num_chars = int(input("Enter number of users: ")), int(input("Enter number of characters: "))
    for i in range(num_users):
        char = string.ascii_letters + string.digits
        random_user_id = ''.join(random.choices(char, k=num_chars))
        print(random_user_id)

#bài tập 3
def rgb_color_gen():
    print("rgb({}, {}, {})".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


               #LEVEL 2
#bài tập 1
def list_of_hexa_colors() -> string:
    num_color = int(input("Enter number of colors: "))
    colors = []
    for i in range(num_color):
        colors.append('#' +''.join(random.choices('0123456789ABCDEF', k=6)))
    return ' '.join(colors)

#bài tập 2
def list_of_rgb_colors():
    num_color = int(input("Enter number of colors: "))
    colors_rgb = []
    for i in range(num_color):
        colors_rgb.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    return colors_rgb

#bài tập 3
def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        print(list_of_hexa_colors())
    elif color_type == 'rgb':
        print(list_of_rgb_colors())

               #LEVEL 3
#bài tập 1
def shuffle_list(lst):
    shuffle_list = lst.copy()
    random.shuffle(shuffle_list)
    return shuffle_list

def unique_list():
    
    number = random.sample(range(10), 7)
    return number

