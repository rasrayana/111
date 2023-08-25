#Moduls
#1 Import modul itself
import lesson8 #without ".py"
lesson8.welcome('bayastan') #calling function "welcome" from modul lesson8.py
lesson8.add(14567, 456789)

#2 
from lesson8 import welcome, add
welcome('Beksultan')
add(69, 96)

#3 import all necessary module at once
from lesson8 import *

welcome('Askar')
add(-1, 2)

