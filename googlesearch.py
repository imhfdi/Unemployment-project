# not Compleate .. !

import os
import webbrowser

os.system('clear')

def googlesearch():
    search = input("\n Google Search For .. 99 for back: ")
    webbrowser.open_new_tab('https://google.com/search?btnG=1&q=%s'% search)

def mainmenu():
    print("Author : Github.com/imhfdi :D")
    print("1: Google Search\nq: for quit ")

mainmenu()
inp1 = input("input : ")
if (inp1 == "1"):
    googlesearch()
    inp2 = input("Do you need search again .. ? (y/N)").lower()
    invalid_input = False

    if (inp2 == "y"):
        os.system('clear')
        googlesearch()
        invalid_input = False
    elif (inp2 == "n"):
        quit()

elif (inp1 == "q"):
    print("Good Luck Buddy .. !")
    invalid_input = True

else:
    print("Invalid Input .. !")

while invalid_input : # this will loop until invalid_input is set to be True
    mainmenu()
