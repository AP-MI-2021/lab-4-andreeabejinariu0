
def citire_lista():
    '''
    Citeste o lista
    :return: lista
    '''
    lista = []
    string_lista = input("Introduceti lista: ")
    string_elemente = string_lista.split(sep=" ")
    for string_element in string_elemente:
        element = float(string_element)
        lista.append(element)
    return lista

def get_nr_pare(lista):
    '''
    Calculeaza numarul elementelor pare din lista
    :param lista: lista in care se cauta
    :return: numarul de elemente pare
    '''
    nr = 0
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            nr = nr + 1

    return nr

def get_same_nr_par(lista1, lista2):
    '''
    Verifica daca listele au acelasi numar de elemente pare
    :param lista1: prima lista
    :param lista2: a doua lista
    :return: rezultatul verificarii
    '''
    if get_nr_pare(lista1) == get_nr_pare(lista2):
        return True
    else:
        return False

def get_intersectie(lista1, lista2):
    '''
    Gaseste si returneaza intersectia celor doua liste
    :param lista1: prima lista
    :param lista2: a doua lista
    :return: intersectia celor doua
    '''
    intersectie = []
    dict_count = {}
    for element in lista1:
        if element not in dict_count:
            dict_count[element] = 1
        else:
            dict_count[element] +=1

    for element2 in lista2:
        if element2 in dict_count and dict_count[element2] > 0:
            intersectie.append(element2)
            dict_count[element2] -= 1

    return intersectie

def get_oglindit(nr):
    '''
    Cauta oglinditul unui numar
    :param nr: numarul
    :return: oglinditul
    '''
    oglindit = 0

    while nr > 0:
        oglindit = oglindit * 10 + nr % 10
        nr = nr // 10

    return oglindit


def is_palindrome(nr):
    '''
    Verifica daca numarul este palindrom
    :param nr: numarul
    :return: rezultatul verificarii
    '''
    oglindit = get_oglindit(nr)
    return oglindit == nr

def if_concat_is_palindrom(lista1,lista2):
    '''
    Verifica daca concatenarea elementelor de pe aceeasi pozitie este palindrom
    :param lista1: prima lista
    :param lista2: a doua lista
    :return: lista palindromelor
    '''
    rezultat = []
    for i in range(0,len(lista1)):
        if is_palindrome(int(str(lista1[i])+ str(lista2[i]))):
            rezultat.append(is_palindrome(int(str(lista1[i])+ str(lista2[i]))))
    return rezultat

def main():
    while(True):
        print("1. Citire liste")
        print("2. Afiseaza daca cele doua liste au acelasi nr de elemente pare")
        print("3. Afiseaza o lista reprezentand intesectia celor 2")
        print("4. Afisati palindroamele obtinute prin concatenarea elementelor de pe acelasi pozitii")
        print("x. Iesire")
        optiune = input("Alege optiunea: ")
        if optiune == "1":
            lista1= citire_lista()
            lista2= citire_lista()
        elif optiune == "2":
            print(get_same_nr_par(lista1,lista2))
        elif optiune == "3":
            print(get_intersectie(lista1, lista2))
        elif optiune == "4":
            print(if_concat_is_palindrom(lista1, lista2))
        elif optiune == "x":
            break

main()