from homework8 import text 
read_text = open('wikipedia.txt', 'r', encoding='utf-8')
print(read_text.read())
read_text.close()
textw = open('wikipedia.txt', 'r', encoding='utf-8')
print(textw.read())
textw.close()


f = open('wikipedia.txt', 'w')
from homework8 import text
f.write(text) 
f.close()

read_txt_file = open('wikipedia.txt', 'r')
print(read_txt_file.read())
read_txt_file.close()
