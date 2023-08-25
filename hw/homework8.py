#1
import random 

def random_language(language_list): 
     language_res = random.choice(language_list) 
     with open('language_res.txt', 'w') as file:
         file.write(language_res) 
         return language_res 
 
language = ["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"] 
random_language(language) 


#2

with open('text.txt', 'w', encoding='utf-8') as text:
    text.write("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularized in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum.""")
with open('text.txt', 'r') as textw:
    print(textw.read())

text = open('my_text', 'w')
text.write("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularized in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum.""")
text.close()

text = open('my_text', 'r')
text.read()
text.close()

#3


