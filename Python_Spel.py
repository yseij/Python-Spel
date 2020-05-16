import random #import random voor random vragen en letters te genereren tijdens het spelen
import time # voor de time.sleep te kunnen gebruiken

lijst_letters = [] #lijst aanmaken van letter maar er zit nog niks in 
lijst_vragen = ["naam van een dier", "landen", "hoofsteden van een land", "auto merken"] #lijst aanmaken van voor ingestelde vragen

letter = input("als u het alfabet wilt gebruiken typet u az, anders type je niks en ga je beginenn met het toevoegen van letters: ")
# een vraag stellen aan de speler met input, het antwoord gelijk stellen aan letter

#Regel 11 tot 14 zorgen er voor dat het alfabet wordt toegevoegd aan de lijst "lijst_letters".
if letter == "az": #if statement die vraagt of letter gelijk is aan "az".
    for i in range(97, 123): #als dat zo is dan komt er een for loop in de range van 97 tot 123 daar gaat het programma door heen lopen.
        toevoeg_letter = chr(i) # de varibale i wordt de hele tijd omgezet naar een chr dat is dus een letter en die wordt gelijk gesteld aan toevoeg_letter
        lijst_letters.append(toevoeg_letter) #toevoeg_letter wordt dan weer aan de lijst met letters toegevoegd.

#Regel 16 tot 21 zorgen er voor dat er een letter wordt toegevoegd aan de lijst "lijst_letters".
else: #als de if statement op regel 11 niet waar is gaat het programma naar de else.
    aantal_letter = int(input("Met hoeveel letters wilt u spelen: ")) # dan vraag je aan de speler hoeveel letters hij wilt toevoegen, dat antwoord stel je gelijk aan aantal_letter
    for i in range(0, aantal_letter): # for loop in een range van 0 tot aantal_letter
        letter = input("Geef een letter die u wilt gebruiken in het spel: ") # dan vraag je aan de speler welke letter hij wilt toevoegen en dat stel je gelijk aan letter
        lijst_letters.append(letter) # dan voeg je de variable letter toe aan de lijst "lijst_letters"
    
print(lijst_letters) # print van de lijst van letters zodat je kunt zien welke zijn toegevoegd


vragen_toevoegen = input("Wilt u vragen toevoegen aan het spel, vul ja in als u dat wilt: ") # vraag of je vragen wilt toevoegen het antwoord wordt gelijk gesteld aan vragen_toevoegen

#Regel 28 tot 33 zorgen er voor dat de vraag wordt toegevoegd aan de lijst "lijst_vragen".
if vragen_toevoegen == "ja": # als je op de vorige vraag ja hebt genantwoord is de if statement waar en ga je vragen toevoegen
    aantal_vragen = int(input("Hoeveel vragen wilt u toevoegen: ")) # # dan vraag je aan de speler hoeveel vragen hij wilt toevoegen, dat antwoord stel je gelijk aan aantal_vragen
    for i in range(0, aantal_vragen): # for loop in een range van 0 tot aantal_vragen
        vraag = input("Geef de vraag die u wilt toevoegen: ") # dan vraag je aan de speler welke vraag hij wilt toevoegen en dat stel je gelijk aan vraag
        lijst_vragen.append(vraag) # dan voeg je de variable vraag toe aan de lijst "lijst_vragen"

spel_beginnen = input("Wilt u het spel beginnen, vul ja in als u dat wilt: ") ## vraag of je het spel wilt beginnen en het antwoord gelijk stellen aan spel_beginnen 

lengte_letter_lijst = len(lijst_letters) - 1 # hier doe je lengte van de lijst min 1 en dat stel je gelijk aan lengte_letter_lijst
lengte_vragen_lijst = len(lijst_vragen) - 1 # hier doe je lengte van de lijst min 1 en dat stel je gelijk aan lengte_vragen_lijst


while spel_beginnen == "ja": # while statement die vraagt of spel_beginnen gelijk is aan ja en als dat waar is gaat het programma in de while loop

    print("vraag:") #tonen van de string "vraag"
    getal_vraag = random.randint(0, lengte_vragen_lijst) # genereren van een random getal en dat gelijk stellen aan getal_vraag
    print(lijst_vragen[getal_vraag]) # aan de hand van de variable getal_vraag een vraag halen uit de lijst "lijst_vragen" en die tonen op het scherm

    print()# een enter op het scherm

    time.sleep(5) # wachten voor 5 seconden
    
    getal_letter = random.randint(0, lengte_letter_lijst) # genereren van een random getal en dat gelijk stellen aan getal_letter
    print(lijst_letters[getal_letter]) # aan de hand van de variable getal_letter een letter halen uit de lijst "lijst_letters" en die tonen op het scherm
    for i in range(0, 5): #een for loop in de range van 0 tot 5
        print() # een enter op het scherm

    geraden = input("Als u de volgende wilt type niks: ") # vragen of je niks wilt intypen voor door te gaan en het antwoord gelijk stellen aan geraden
    if geraden == "": # if statement die vraagt of geraden gelijk is aan een lege string
        spel_beginnen = "ja" # als de if stament waar is dan zal spel_beginnen gelijk gesteld worden aan ja en is de while loop op regel 40 weer waar.
# als de if statement nier waar is dan is de while ook niet waar en stopt het programma.