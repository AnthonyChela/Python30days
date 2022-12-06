import pyautogui as pt
import time

limit = input("Cantidad de mensajes: ")
message = input("Mensaje: ")
i=0

time.sleep(3)

'''buenas practicas es mejor
usar el for en vez del while
y revisar lenguajes de alto nivel''' 

while i < int(limit):
    pt.typewrite(message)
    pt.press("enter")
    i += 1


'''Segunda Opcion
import pywhatkit as pk

second = 10
pk.sendwhatmsg("+xx", "Holis", 13, )
pk.sendwhatmsg_instantly("+xx","Holis")
pk.sendwhatmsg("+xx", "k",15,7)

con tiempo especifico
from datetime
import datetime
import time
'''