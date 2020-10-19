import lista_cuvinte as ls
import desen as d
import random
import os
import time


cuvant = random.choice(ls.liste).lower()
nr_incercari = 10
charactere_gasite = []
charactere_negasite = []

while nr_incercari > 0:
    character = input('\nIntroduceti un caracter: ').lower()

    if character in charactere_gasite or character in charactere_negasite:
        print('Ati mai tastat deja acest caracter!')
        nr_incercari -= 1

    elif character in cuvant:
         charactere_gasite.append(character)

    elif character not in cuvant:
         charactere_negasite.append(character)
         nr_incercari -= 1
    

    
    time.sleep(1.5)          
    os.system("cls")

    lista_litere = [
        litera if litera in charactere_gasite else '_' for litera in cuvant]
    
    print('=='* len(lista_litere),'\n')
    print(' '.join(lista_litere), '\n')
    print('=='* len(lista_litere))
    print('\nCaractere gasite: ', ' '.join(charactere_gasite), '\n \n')
    # print(cuvant)
    print('Mai aveti:', nr_incercari, 'incercari.\n')

    if nr_incercari >= 8:
        print(d.desen_hgang[0])
    elif nr_incercari >= 6 and nr_incercari < 8:
        print(d.desen_hgang[1])
    elif nr_incercari >= 4 and nr_incercari < 6:
        print(d.desen_hgang[2])
    elif nr_incercari >= 1 and nr_incercari < 4:
        print(d.desen_hgang[3])
    elif nr_incercari == 0:
        print(d.desen_hgang[4])




    if '_' not in lista_litere:
        print('Felicitari! Ati castigat!')
        break

