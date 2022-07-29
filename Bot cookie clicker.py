
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#ouverture de edge
driver = webdriver.Edge()
driver.get("https://orteil.dashnet.org/cookieclicker/")

#Click sur le gros cookies
cookieclick = driver.find_element_by_id("bigCookie")

#cookies
cookies = driver.find_element_by_id("cookies")

#products
products = driver.find_element_by_id("products")

#print(products.text)

def test(produit):
    try:
        driver.find_element_by_id(produit)
    except:
        return False
    else:
        return True

def nombre(webelements,i):
    #dix
    if(len(webelements)-i == 2 ):
        return [0,0]
    #cent
    elif(len(webelements)-i == 3):
        return [1,0]
    I=i+1
    #mille
    if (webelements[I] == ","):
        return [2,1]
    elif(webelements[I+1] == ","):
        return [2,2]
    elif(webelements[I+2] == ","):
        return [2,3]
    

    #dix
    if webelements[I+1] == " " or webelements[I+1] == "\n":
        return [0,0]
    #cent
    if webelements[I+2] == " " or webelements[I+2] == "\n":
        return [1,0]
    for L in range (i+1,len(webelements)):
        if webelements[I] == "." and len(webelements) >= I+5:
            #million
            if webelements[I+5] == "m":
                return [3,L-i]
            #Billion
            elif webelements[I+5] == "b":
                return [4,L-i]
            #trillion
            elif webelements[I+5] == "t":
                return [5,L-i]
            #quadrillion
            elif webelements[I+5] == "q" and webelements[I+5] == "a":
                return [6,L-i]
            #quintillion
            elif webelements[I+5] == "q":
                return [7,L-i]
            #sextillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #septillion
            elif webelements[I+5] == "s":
                return [9,L-i]
            #octillion
            elif webelements[I+5] == "s":
                return [10,L-i]
            #nonillion
            elif webelements[I+5] == "s":
                return [11,L-i]
                """
            #decillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #undecillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #duodecillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #tredecillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #quattuordecillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #quindecillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #sexdecillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #septendecillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #octodecillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #novemdecillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #vigintillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #unvigintillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #duovigintillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #trevigintillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #quattuorvigintillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #quinvigintillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #sexvigintillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #septenvigintillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #octovigintillion
            elif webelements[I+5] == "s":
                return [8,L-i]
            #novemvigintillion
            elif webelements[I+5] == "s":
                return [8,L-i]
                """
            
    return [-1,0]

def Convertion(Element, i):
    Elem = nombre(Element,i)
    if Elem[0] == 0:
        return [int(Element[i]+Element[i+1]),Elem[0]]
    elif Elem[0] == 1:
        return [int(Element[i]+Element[i+1]+Element[i+2]),Elem[0]]
    elif Elem[0] > 1:
        if Elem[1] == 1 :
            return [int(Element[i]+Element[i+2]+Element[i+3]+Element[i+4]),Elem[0]]
        elif Elem[1] == 2 :
            return [int(Element[i]+Element[i+1]+Element[i+3]+Element[i+4]+Element[i+5]),Elem[0]]
        elif Elem[1] == 3 :
            return [int(Element[i]+Element[i+1]+Element[i+2]+Element[i+4]+Element[i+5]+Element[i+6]),Elem[0]]
    else:
        return [int(Element[i]),Elem[0]]

def nbBuy(produit):
    try:
        i = len(produit) -1
        while(produit[i] != " "):
            i -=1
        if (Convertion(produit, i) < 250):
            return True
    except:
        return True
    return False


def buyproduct():
    if(test("product18")):
        #Idleverse
        try:
            Idleverse = driver.find_element_by_id("product18")
            prixIdleverse = Convertion(Idleverse.text, 10)
        except:
            None
        else:
            if(nbcookies[0] >= prixIdleverse[0] and nbcookies[1] >= prixIdleverse[1] and nbBuy(Idleverse.text)):
                try: 
                    driver.find_element_by_id("product18").click()
                except:
                    None
    if(test("product17")):
        #JSConsole
        try:
            JSConsole = driver.find_element_by_id("product17")
            prixJSConsole = Convertion(JSConsole.text, 18)
        except:
            None
        else:
            if(nbcookies[0] >= prixJSConsole[0] and nbcookies[1] >= prixJSConsole[1] and nbBuy(JSConsole.text)):
                try: 
                    driver.find_element_by_id("product17").click()
                except:
                    None
    if(test("product16")):
        #Fractal
        try:
            Fractal = driver.find_element_by_id("product16")
            prixFractal = Convertion(Fractal.text, 14)
        except:
            None
        else:
            if(nbcookies[0] >= prixFractal[0] and nbcookies[1] >= prixFractal[1] and nbBuy(Fractal.text)):
                try: 
                    driver.find_element_by_id("product16").click()
                except:
                    None
    if(test("product15")):
        #Chancemaker
        try:
            Chancemaker = driver.find_element_by_id("product15")
            prixChancemaker = Convertion(Chancemaker.text, 6)
        except:
            None
        else:
            if(nbcookies[0] >= prixChancemaker[0] and nbcookies[1] >= prixChancemaker[1] and nbBuy(Chancemaker.text)):
                try: 
                    driver.find_element_by_id("product15").click()
                except:
                    None
    if(test("product14")):
        #Prism
        try:
            Prism = driver.find_element_by_id("product14")
            prixPrism = Convertion(Prism.text, 6)
        except:
            None
        else:
            if(nbcookies[0] >= prixPrism[0] and nbcookies[1] >= prixPrism[1] and nbBuy(Prism.text)):
                try: 
                    driver.find_element_by_id("product14").click()
                except:
                    None
    if(test("product13")):
        #Antimatter
        try:
            Antimatter = driver.find_element_by_id("product13")
            prixAntimatter = Convertion(Antimatter.text, 20)
        except:
            None
        else:
            if(nbcookies[0] >= prixAntimatter[0] and nbcookies[1] >= prixAntimatter[1] and nbBuy(Antimatter.text)):
                try: 
                    driver.find_element_by_id("product13").click()
                except:
                    None
    if(test("product11")):
        #Time
        try:
            Time = driver.find_element_by_id("product11")
            prixTime = Convertion(Time.text, 13)
        except:
            None
        else:
            if(nbcookies[0] >= prixTime[0] and nbcookies[1] >= prixTime[1] and nbBuy(Time.text)):
                try: 
                    driver.find_element_by_id("product11").click()
                except:
                    None
    if(test("product10")):
        #Portal
        try:
            Portal = driver.find_element_by_id("product10")
            prixPortal = Convertion(Portal.text, 7)
        except:
            None
        else:
            if(nbcookies[0] >= prixPortal[0] and nbcookies[1] >= prixPortal[1] and nbBuy(Portal.text)):
                try: 
                    driver.find_element_by_id("product10").click()
                except:
                    None
    if(test("product9")):
        #Lab
        try:
            Lab = driver.find_element_by_id("product9")
            prixLab = Convertion(Lab.text, 12)
        except:
            None
        else:
            if(nbcookies[0] >= prixLab[0] and nbcookies[1] >= prixLab[1] and nbBuy(Lab.text)):
                try: 
                    driver.find_element_by_id("product9").click()
                except:
                    None
    if(test("product8")):
        #Shipment
        try:
            Shipment = driver.find_element_by_id("product8")
            prixShipment = Convertion(Shipment.text, 9)
        except:
            None
        else:
            if(nbcookies[0] >= prixShipment[0] and nbcookies[1] >= prixShipment[1] and nbBuy(Shipment.text)):
                try: 
                    driver.find_element_by_id("product8").click()
                except:
                    None
    if(test("product7")):
        #Wizard
        try:
            Wizard = driver.find_element_by_id("product7")
            prixWizard = Convertion(Wizard.text, 13)
        except:
            None
        else:
            if(nbcookies[0] >= prixWizard[0] and nbcookies[1] >= prixWizard[1] and nbBuy(Wizard.text)):
                try: 
                    driver.find_element_by_id("product7").click()
                except:
                    None
    if(test("product6")):
        #Temple
        try:
            Temple = driver.find_element_by_id("product6")
            prixTemple = Convertion(Temple.text, 7)
        except:
            None
        else:
            if(nbcookies[0] >= prixTemple[0] and nbcookies[1] >= prixTemple[1] and nbBuy(Temple.text)):
                try: 
                    driver.find_element_by_id("product6").click()
                except:
                    None
    if(test("product5")):
        #Bank
        try:
            Bank = driver.find_element_by_id("product5")
            prixBank = Convertion(Bank.text, 5)
        except:
            None
        else:
            if(nbcookies[0] >= prixBank[0] and nbcookies[1] >= prixBank[1] and nbBuy(Bank.text)):
                try: 
                    driver.find_element_by_id("product5").click()
                except:
                    None
    if(test("product4")):
        #Factory
        try:
            Factory = driver.find_element_by_id("product4")
            prixFactory = Convertion(Factory.text, 8)
        except:
            None
        else:
            if(nbcookies[0] >= prixFactory[0] and nbcookies[1] >= prixFactory[1] and nbBuy(Factory.text)):
                try: 
                    driver.find_element_by_id("product4").click()
                except:
                    None
    if(test("product3")):
        #Mine
        try:
            Mine = driver.find_element_by_id("product3")
            prixMine = Convertion(Mine.text, 5)
        except:
            None
        else:
            if(nbcookies[0] >= prixMine[0] and nbcookies[1] >= prixMine[1] and nbBuy(Mine.text)):
                try: 
                    driver.find_element_by_id("product3").click()
                except:
                    None
    if(test("product1")):
        #Grandmere
        try:
            GM = driver.find_element_by_id("product1")
            prixGM = Convertion(GM.text, 8)
        except:
            None
        else:
            if(nbcookies[0] >= prixGM[0] and nbcookies[1] >= prixGM[1] and nbBuy(GM.text)):
                try: 
                    driver.find_element_by_id("product1").click()
                except:
                    None
    if(test("product0")):
        #Cursor
        try:
            cursor = driver.find_element_by_id("product0")
            prixcursor = Convertion(cursor.text, 7)
        except:
            None
        else:
            if(nbcookies[0] >= prixcursor[0] and nbcookies[1] >= prixcursor[1] and nbBuy(GM.text)):
                try: 
                    driver.find_element_by_id("product0").click()
                except:
                    None
    if(test("product2")):
        #Farm
        try:
            Farm = driver.find_element_by_id("product2")
            prixFarm = Convertion(Farm.text, 5)
        except:
            None
        else:
            if(nbcookies[0] >= prixFarm[0] and nbcookies[1] >= prixFarm[1] and nbBuy(Farm.text)):
                try: 
                    driver.find_element_by_id("product2").click()
                except:
                    None

def BuyAchevements():
    try:
        driver.find_element_by_id("upgrade0").click()
    except:
        None

def Clickperiodique():
    nb=0
    while(nb<50):
        cookieclick.click()
        nb+=1

def iziachivements():
    driver.find_element_by_id("statsButton").click()
    driver.find_element_by_class_name("tinyCookie").click()
    driver.find_element_by_id("logButton").click()
    for i in range(50):
        driver.find_element_by_id("commentsText").click()

nbcookies=[0,0]

driver.implicitly_wait(10)

iziachivements()
while(nbcookies[1] != 5):
    #CLICK
    Clickperiodique()
    driver.implicitly_wait(1)
    #nbcookie
    nbcookies= Convertion(cookies.text,0)
    #buyachevements
    BuyAchevements()
    #buyproducts
    buyproduct()

driver.quit()
