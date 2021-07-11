import json 
import time
from bs4 import BeautifulSoup
from lxml import etree
import requests 

############ Données qu'on a besoin ####################
calcul = False # True si on va calculer l'échange d'un montant
op = None #'Achat' ou 'Vente'
montant = None
code = None

########################################################

link = 'https://www.dinartunisien.com/fr/cours-devises-banques-tunisie'
link1 = 'https://www.dinartunisien.com'
time.sleep(2)
#Extract Information
website = requests.get(link)
soup = BeautifulSoup(website.text, 'html.parser')

dom = etree.HTML(str(soup))

#Extraire la liste des banques et les liens de ces pages

list_bank = []
list_link = []

k=1
elt = dom.xpath('/html/body/div[4]/div/div[1]/h2/a')

while len(elt) > 0 :
    for el in elt :
        bk = el.text
        list_bank.append(bk[1:len(bk)-1] )
        list_link.append(link1 + el.get('href'))
    k +=1
    elt = dom.xpath('/html/body/div[4]/div/div[' + str(k) + ']/h2/a')

time.sleep(2)

print('********************************************')
print('Voici la liste des banques : ')
print(list_bank)

bank = input("Choisir la banque que vous voulez !!")
print('********************************************')

time.sleep(2)

#supposant que le nom du banque est entré
nom_bank = bank
#déterminer le lien du page de cette banque
ind = list_bank.index(nom_bank)
l_bank = list_link[ind]
print(l_bank)

#Accéder a cette lien
time.sleep(2)
website1 = requests.get(l_bank)
soup1 = BeautifulSoup(website1.text, 'html.parser')
dom1 = etree.HTML(str(soup1))

time.sleep(2)

############################################ Listes des codes #####################################
list_code = []
m=1
elt1 = dom1.xpath('/html/body/div[4]/div[1]/div[1]/table[1]/tbody/tr[1]/td[2]')

while len(elt1) > 0 :
    for el1 in elt1 :
        bk1 = el1.text
        list_code.append(bk1[1:len(bk1)-1] )
        
    m +=1
    elt1 = dom1.xpath('/html/body/div[4]/div[1]/div[1]/table[1]/tbody/tr[' + str(m) + ']/td[2]')
time.sleep(2)

############################################ Listes des Achats #####################################

Achats = []
p=1
elt2 = dom1.xpath('/html/body/div[4]/div[1]/div[1]/table[1]/tbody/tr[1]/td[4]')

while len(elt2) > 0 :
    for el2 in elt2 :
        bk2 = el2.text
        Achats.append(bk2[1:len(bk2)-1] )
        
    p +=1
    elt2 = dom1.xpath('/html/body/div[4]/div[1]/div[1]/table[1]/tbody/tr[' + str(p) + ']/td[4]')
time.sleep(2)

############################################ Listes des Ventes #####################################

Ventes = []
g=1
elt3 = dom1.xpath('/html/body/div[4]/div[1]/div[1]/table[1]/tbody/tr[1]/td[5]')

while len(elt3) > 0 :
    for el3 in elt3 :
        bk3 = el3.text
        Ventes.append(bk3[1:len(bk3)-1] )
        
    g +=1
    elt3 = dom1.xpath('/html/body/div[4]/div[1]/div[1]/table[1]/tbody/tr[' + str(g) + ']/td[5]')

time.sleep(2)


############################################# Calcul ##############################################

if calcul :
    ind_code = list_code.index(code)
    if op == 'Achat':
        nouv = montant * Achats[ind_code]
        print(nouv)
    elif op == 'vente' :
        nouv = montant * Achats[ind_code]
        print(nouv)