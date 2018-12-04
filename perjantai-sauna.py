#-------------------------------------------------------------------------------
# Name:        Ebin Sauna Sim
# Purpose:      Be funny
#
# Author:      Jani "Keisari" Laamanen
#
# Created:     05.12.2017
# Copyright:   (c) Jani Laamanen 2017
# Licence:     Bigger than yours
#-------------------------------------------------------------------------------

#Viiva
def viiva():
    print("---------------")

#miten peliä pelataan
def kuinka():
    viiva()
    print ("Pelin tarkoitus on olla mahdollisimman kauan saunassa ilman että kalja loppuu, kuolet tai sauna kylmentyy")
    viiva()
    print ("Vuorossa voit joko juoda tai heittää löylyä")
    print ("Löylyn heittäminen nostaa saunan lämpötilaa sekä nostaa piste kerrointa")
    print ("Muista kuitenkin että maaginen 100 asteinen sauna tappaa heti. Se on fakta!")
    viiva()
    print ("Juominen antaa sinulle pisteitä 1x keräämäsi kerroin sekä puolittaa kertoimen")
    print ("Muista myös että kun juot et voi heittää löylyä ja sauna kylmenee")
    print ("ja kukaan ei pidä kylmästä saunasta")
    viiva()
    print ("Muista kuitenkin että vaikka saunavuoro onkin sinun kaikki eivät sitä kunnioita")
    print ("ja saattavat tunkeutua saunaan vuorollasi tehden mitä sattuu")
    viiva()
    viiva()
    print ("[1] Pelaa")
    print ("[3] lopeta")

    x = int(input("Mitä teet?"))

    if x == 1:
        peli()
    elif x == 3:
        print ("kys")
    else:
        print ("Et osaa yksinkertaisia Ohjeita seurata?")

#päävalikko
def valikko():
    print ("[1] Pelaa")
    print ("[2] Kuinka pelata")
    print ("[3] lopeta")

    x = int(input("Mitä teet?"))
    if x == 1:
        peli()

    elif x == 2:
        kuinka()
    elif x == 3:
        print ("Hei hei")
    else:
        print ("Et osaa yksinkertaisia Ohjeita seurata?")
        viiva()
        valikko()

#määrittää lähtö lämmön
def asetukset(x):
    if x == 1:
        lampo = 20
        return lampo
    elif x == 2:
        lampo = 30
        return lampo
    elif x == 3:
        lampo = 40
        return lampo

    elif x == 4:
        lampo = 50
        return lampo
    else:
        print ("*Virheellinen syöttö*")
        peli()


#jos lämpö liian kova
def kuolit(kalja, pisteet):
    viiva()
    viiva()
    print ("Saunasta tuli liian kuuma ja paloit elävältä")
    print ("Sinulla oli jäljellä ", kalja, "kaljaa")
    print ("Loppu pisteesi: ",pisteet)
    viiva()
    viiva()
    x = (input("Paina enter jatkaaksesi"))
    valikko()


#jos kalja loppuu
def olut(pisteet):
    viiva()
    viiva()
    print ("Ei jumalauta, kalja loppui")
    print ("Loppu pisteesi:",pisteet)
    viiva()
    viiva()
    x = (input("Paina enter jatkaaksesi"))
    valikko()



#sauna kylmenee
def kylma(kalja,pisteet):
    viiva()
    viiva()
    print ("Perseeet olalla ja kiuas kylmänä.")
    print ("Sinulla oli jäljellä ", kalja, "kaljaa")
    print ("Loppu pisteesi: ",pisteet)
    viiva()
    viiva()
    x = (input("Paina enter jatkaaksesi"))
    valikko()

#jos joku tulee saunaa aka yllarit
def vieras(kalja, lampo):
    import random
    x = random.randint(1,5)
    if x == 1:
        viiva()
        print("Saunaan astuu naapurin Timppa ja vie kaljan")
        viiva()
        siirto = ["kalja", kalja - 1]
        return siirto
    elif x == 2:
        y = random.randint(2,12)
        viiva()
        print("Saunaan eksyy ihminen väärällä saunavuorolla. Säikähdät ja pudotat", y, "kaljaa.")
        viiva()
        siirto = ["kalja", kalja - y]
        return siirto
    elif x == 3:
        y = random.randint(10,40)
        viiva()
        print("Löylyn henki siunaa saunan ja kuumentaa sitä", y, "astetta")
        viiva()
        siirto = ["lampo",lampo + y]
        return siirto
    elif x == 4:
        y = random.randint(10,40)
        viiva()
        print("Jonkun lapsi juoksee saunaan ja avaa sen oven viilentäen saunaa",y , "astetta")
        viiva()
        siirto = ["lampo", lampo - y]
        return siirto
    elif x == 5:
        viiva()
        print("Löydät lauteiden välistä kaljan")
        viiva()
        siirto = ["kalja", kalja + 1]
        return siirto

#tarkistaa onko liian kuuma, kylmä tai loppuiko kalja
def loppuiko(alku_lampo,lampo, kalja, pisteet):
       if lampo >= 100:
                pelaaja = "ei pelaa"
                kuolit(kalja,pisteet)
       elif lampo < alku_lampo//2:
            pelaaja = "ei pelaa"
            kylma(kalja, pisteet)
       elif kalja == 0:
            pelaaja = "ei pelaa"
            olut(pisteet)

#itsepeli
def pelaa(juoma, kuuma, vaikeus):
    import random
    kerroin = 1
    pisteet = 0
    kierros = 0
    yllari1 = random.randint(1,6)
    yllari2 = random.randint(7,12)
    yllari3 = random.randint(13,18)
    yllari4 = random.randint(19,24)
    alku_lampo = kuuma
    lampo = kuuma
    kalja = juoma
    aste = vaikeus
    pelaaja = "pelaa"
    while pelaaja == "pelaa":
        if kierros == yllari1 or kierros == yllari2 or kierros == yllari3 or kierros == yllari4 :
            x = vieras(kalja, lampo,)
            if x[0] == "kalja":
                kalja = x[1]
            elif x[0] == "lampo":
                lampo = x[1]

        loppuiko(alku_lampo,lampo,kalja,pisteet)

        viiva()
        print ("Kertoimesi:",kerroin,"|","Pitseesi:",pisteet,"|","Kaljaa:",kalja,
                "|","Saunan lämpötila :", lampo)
        print ("[1]Juo")
        print ("[2]Lisää löylyä")
        x = int(input("Mitä teet?"))

        if x == 1:
            pisteet = (1 * kerroin) + pisteet
            if kerroin > 1:
                kerroin = kerroin//2
            else:
                kerroin = kerroin
            kalja = kalja - 1
            kierros = kierros + 1
            if aste > 1:
                lampo = lampo - (aste * 2)
            lampo = lampo - ((aste*10)//2)

        elif x == 2 and aste > 1:
            lampo = (aste * 5) + lampo
            kerroin = kerroin * aste
            kierros = kierros + 1

        elif x == 2 and aste == 1:
            lampo = (aste * 10) + lampo
            kerroin = kerroin * 2 + aste
            kierros = kierros + 1
        else:
            print ("*Virheellinen syöttö*")

#vaikeus asteen valinta
def peli():
    viiva()
    print ("Valitse vaikeus aste:")
    print ("[1]Helppo")
    print ("[2]Keski vaikea")
    print ("[3]Vaikea")
    print ("[4]Sauna Timo")
    aste = int(input("Mitä teet?"))

    lampo = asetukset(aste)
    kalja = 24

    pelaa(kalja, lampo, aste)

#MAIN
print ("Perjantai sauna simulaattori")
print ("By Laama Tech")
valikko()

