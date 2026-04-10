from time import sleep
from random import choice
from dicionario import vocabulario


while True:
    # Sorteio da palavra
    palavra = choice(vocabulario).upper()
    print("Jogo da forca em Python")
    print()
    print(f"Nossa palavra tem {len(palavra)} letras")
    letras = []
    oculta = ['_'] * len(palavra)
    print(' '.join(oculta))
    cont = 0

    # Esconder palavra do usuario
    while "_" in oculta:
        print()
        if letras:
            print(f'Digitadas: {letras}')
        
        #Chegem se entrada é letra
        while True:
            busca = input("Digite uma letra para advinhar: ").upper().strip()
            if len(busca) == 1 and busca.isalpha():
                break
            print('Erro, digite apenas UMA LETRA.')
        
        #Verificar se letra ja foi digitada
        print("=" * 33)
        if busca in letras:
            print(f"A letra {busca} já foi digitada.")
            continue

        letras.append(busca)
        print()

        #Buscar letra nova na palavra escolhida
        if busca in palavra:
            for c, i in enumerate(palavra):
                if busca == i:
                    oculta[c] = busca
            print(' '.join(oculta))
            print("." * 30)

        #Acresenta uma parte do boneco na forca caso não tenha letra na palavra escolhida
        else:
            cont += 1
            print(f'A palavra nao tem a letra {busca}! Tente de novo.')
            print(' '.join(oculta))
            if cont == 1:
                print(" ____")
                print("|    O")
            elif cont == 2:
                print(" ____")
                print("|    O")
                print("|    |")
            elif cont == 3:
                print(" ____")
                print("|    O")
                print("|   /|")
            elif cont == 4:
                print(" ____")
                print("|    O")
                print("|   /|\\")
            elif cont == 5:
                print(" ____")
                print("|    O")
                print("|   /|\\")
                print("|   /")
            elif cont == 6:
                print(" ____")
                print("|    O")
                print("|   /|\\")
                print("|   / \\")
                print("Enforcou")
                print(f"A palavra é {palavra}")
                break
        
        if "_" not in oculta:
            print("Você venceu!")

    #Looping para jogar novamente
    while True:
        continuar = input('Quer jogar novamente? [S/N]').strip().upper()
        if continuar in 'SN':
            break
        print('Digite [S/N]')
    
    #Fim do programa
    if continuar == 'N':
        break
