"""
Projekt2.py:

__author__  = "Valter Carlens"
__version__ = "1.0.0"
__email__   = "Valter.carlens@elev.ga.ntig.se"
"""


# importerar os för att sudda allt onödigt på skärmen
import os
import time
from colors import bcolors
#deklarerar listan och vilka namn som ska vara i den från början
vänner_lista = ["Peter","Petter", "Per"]

#gör en funktion som printar ut listan 1 -> x
def list_name():
    number=1
    for name in vänner_lista:
        print(bcolors.PURPLE + f"{number} {name} ")
        number+=1

def add_name(name):
    vänner_lista.append(name)


while True:
    try:
        #ger användaren alternativ för choice den vill göra med listan
        os.system("cls")
        print(bcolors.BLUE+ "--MINA VÄNNER--")
        list_name()
        print(bcolors.BLUE + f"Du har {len(vänner_lista)} namn i din lista")
        choice=input(bcolors.GREEN + f"\n---------- \n1.lägg till \n2.ändra \n3.ta bort \n4.sortera listan \nenter.avsluta \n----------\n:")
        if choice == "":
            print(f"\n---DIN FÄRDIGA LISTA---")
            list_name()
            print(bcolors.BLUE + f"Du har {len(vänner_lista)} namn i din lista")
            print(bcolors.BLUE + "Färdig med listan!")
            break
        
        #gör choice till en integer
        choice=int(choice)

        #Lägger till nytt namn
        if choice == 1:
            time.sleep(0.5)
            name=input(bcolors.CYAN + "Nytt namn: ")
            tempname=name[0].upper()+name[1:len(name)]
            add_name(tempname)
            time.sleep(0.5)
            list_name()
        
        #ändrar namn
        elif choice == 2:
            time.sleep(0.5)
            name_ändra=int(input(bcolors.CYAN + f"Vilket namn vill du ändra? (1-{len(vänner_lista)})"))
            time.sleep(0.5)
            new_name=(input("Vad ska det nya namnet vara? "))
            vänner_lista[name_ändra -1]=new_name
            time.sleep(0.5)
            list_name()

        #tar bort namn
        elif choice == 3:
            time.sleep(0.5)
            vänner_tabort=input(bcolors.CYAN + "Vilket namn vill du ta bort? ") 
            try:
                vänner_lista.remove(vänner_tabort)
                time.sleep(0.5)
                list_name()
            except ValueError:
                time.sleep(0.5)
                print(bcolors.RED + "Namnet finns inte, välj ett namn som finns i listan\n")
                time.sleep(3)
                continue
        
        elif choice ==4:
            time.sleep(2)
            vänner_lista.sort()
        #ser till så att man bara kan skriva in alternativen 1-3 som anges
        elif choice >4:
            time.sleep(0.5)
            print(bcolors.RED + "Välj mellan alternativen 1-4")
            time.sleep(2)
            ValueError
            continue

        #ser till så att man vara kan skriva in alternativen 1-3 som anges
        elif choice <1:
            time.sleep(0.5)
            print(bcolors.RED + "Välj mellan alternativen 1-4")
            time.sleep(2)
            ValueError
            continue

        #om användaren skriver in något annat en en integer så blir det error
    except ValueError:
        print(bcolors.RED + "Fel input!")
        time.sleep(2)
        continue

    #gör en while loop för avslutningsprogrammet 
    while True:
        os.system("cls")
        break