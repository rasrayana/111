# #file
# f = open('geeks.txt', 'w')
# f.write("hello world and geeks it courses")
# f.close()

# read_txt_file = open('geeks.txt', 'r')
# print(read_txt_file.read())
# read_txt_file.close()

# read_python_code_file = open('homework7.py', 'r', encoding ='utf-8')
# print(read_python_code_file.read())
# read_python_code_file.close()

# text = """Weight of the world on your shoulders
# I'll kiss your waist and ease your mind
# I must be favored to know ya
# I'll take my hands and trace your lines
# It's the way that you can ride
# It's the way that you can ride (oh-oh, oh-oh)
# Think I met you in another life
# So break me off another time (oh-oh, oh-oh)
# You wrap around me and you give me life
# And that's why night after night
# I'll be fuckin' you right
# Monday, Tuesday, Wednesday, Thursday, Friday
# Saturday, Sunday (a week)
# Monday, Tuesday, Wednesday, Thursday, Friday
# Seven days a week
# Every hour, every minute, every second
# You know night after night
# I'll be fuckin' you right, seven days a week
# You love when I jump right in
# All of me, I'm offering
# Show you what devotion is
# Deeper than the ocean is
# Wind it back, I'll take it slow
# Leave you with that afterglow
# Show you what devotion is
# Deeper than the ocean is
# It's the way that you can ride
# It's the way that you can ride (oh-oh, oh-oh)
# Think I met you in another life
# So break me off another time (oh-oh, oh-oh)
# You wrap around me and you give me life
# And that's why night after night
# I'll be fuckin' you right, oh-oh-oh-oh"""
# lyrics_seven_days = open('lyrics_seven_days.txt', 'w', encoding='utf-8')
# lyrics_seven_days.write(text)
# lyrics_seven_days.close()

# read_text = open('lyrics_seven_days.txt', 'r', encoding='utf-8')
# print(read_text.read())
# read_text.close()

# newjeans_txt = open('newjeans.txt', 'w', encoding='utf-8')
# newjeans_txt.write('Asap\n')
# newjeans_txt.write('Cool with you\n')
# newjeans_txt.write('Cookie\n')
# newjeans_txt.close()

# new_newjeans_txt = open('newjeans_txt', 'a+', encoding='utf-8')
# new_newjeans_txt.write('OMG\n')
# new_newjeans_txt.close()

with open('courses.txt', 'w', encoding='utf-8') as courses:
    courses.write('Geeks\n')
    courses.write('Mad Devs')
with open('courses.txt', 'r') as read_courses:
    print(read_courses.read())

with open('hello.py', 'w', encoding='utf-8' ) as py:
    py.write("print('Hello world')")

with open('lesson8.py', 'a+', encoding='utf-8') as lesson:
    lesson.write('name = "Nurbolot"\n')
    lesson.write('print("name")\n')

def welcome(name:str):
    print("Hello", name)

def add(num_1, num_2):
    print(num_1 + num_2)