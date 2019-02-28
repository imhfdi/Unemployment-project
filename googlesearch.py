#Project not complate .. !

import webbrowser
import os

os.system('clear')
def googlesearch():
        search = input("\n Google Search For .. :")
        webbrowser.open_new_tab('https://google.com/search?btnG=1&q=%s' % search)
        op2 = ("Do You Want Search Again .. ? (y/N)")
        if (op2 == "y"):
            googlesearch()
            invalid_input = False

        elif (op2 == "Y"):
            googlesearch()
            invalid_input = False

        elif (op2 == "n"):
           mainmeu()
           invalid_input = False
        else:
            print("OWK ..")
            invalid_input = False
invalid_input = True
def mainmenu():
     print("What Do You Want .. ?")
     op = input("1 or 2 : ")
     if (op == "1"):
         invalid_input = False
         googlesearch()

     elif (op == "2"):
         print("Good by ..\nSee You Again ..:)")

     else:
         print("Please Type 1 Or 2")
         mainmenu()
while invalid_input : # this will loop until invalid_input is set to be True
    mainmenu()
