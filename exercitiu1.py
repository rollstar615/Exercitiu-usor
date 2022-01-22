def lista_double(lista):
    rezultat=[]
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i]==2*lista[j]:
                rezultat.append(lista[j])
    return rezultat

def verif_lista():
    assert lista_double([1,2,3,4,5,6])==[1,2,3]
    assert lista_double([2,6,8,9,10,12,16])==[12,16]
    assert lista_double([0,3,7,8,13,26,13,14])==[0,13,7]

def read_list():
    lista=[]
    nr=int(input("cate numere doriti: "))
    for i in range(nr):
        lista.append(int(input("dati al {}-lea numar:".format(i+1))))
    return lista

def afisare_lista(lista):
    lista_afisar=lista_double(lista)
    print("numerele cu dublu din functie sunt:", lista_afisar)

def show_menu():
    print("1. Citire lista")
    print("2. Afisare numerele care au dublul in lista")
    print("x. iesire")

def interface():
    lista = []
    while True:
        show_menu()
        op = input("Optiune: ")
        if op == "1":
            lista = read_list()
        elif op == "2":
            afisare_lista(lista)
        elif op == "x":
            break
        else:
            print("invalid")
interface()
