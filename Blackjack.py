import random

dois_jogadores = input("Você gostaria de jogar em duas pessoas?(sim/não): ")
#Jogo para dois
if dois_jogadores == "sim":
    jogador_1 = input("Qual nome do primeiro jogador?: ")
    jogador_2 = input("Qual nome do segundo jogador?: "

    d_jogador1 = 1000
    aposta_1 = 0
    d_jogador2 = 1000
    aposta_2 = 0
    print ("Ok, vocês tem 1000 dinheiros cada para apostar. {0}, você começa jogando e depois é o(a) {1}".format(jogador_1, jogador_2))
    #Jogada jogador 1
    aposta_1 = int(input("{0} quanto você quer apostar?"))
    while d_jogador1 > 0 and d_jogador1 >= aposta_1:
        b = int(input('Com quantos baralhos deseja jogar?: '))
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4*b
        mao = []
        
        for i in range(2):
            random.shuffle(deck)
            carta = deck.pop()
            mao.append(carta)
        print (mao)
        
        j = 0
        soma_1 = 0
        while j < len(mao):
        carta = mao[j]
        if carta == "J" or carta == "Q" or carta == "K":
            soma_1 += 10
        elif carta == "A":
            if soma_1 >= 11:
                soma_1 += 1
            else: 
                soma_1 += 11
        else: 
            soma_1 += carta
        j+=1
        print ('Sua soma é', soma_1)

        mao_CPU = []
        for i in range(2):
            random.shuffle(deck)
            carta_CPU = deck.pop()
            mao_CPU.append(carta_CPU)

        print ("O dealer virou a carta", mao_CPU[0])

        if mao_CPU[0] == "Q" or mao_CPU[0] == "J" or mao_CPU[0] == "K" :
            mao_CPU[0] = 10
        elif mao_CPU[0] == "A":
            mao_CPU[0] = 11
        
        while soma_1 < 21:
            ajuda = input("Você deseja receber ajuda no que fazer?(sim/não)")

            if ajuda == "sim":
                if soma_1 <= 11:
                    print("Uhmm. Acho que você deveria comprar mais uma carta.")
                elif soma_1 >= 12 and mao_CPU[0] <= 6:
                    print("Uhmm. Acho que você não deveria comprar mais cartas.")
                elif soma_1 >= 12 and soma_1 < 17 and mao_CPU[0] >= 7:
                    print("Uhmm. Acho que você deveria comprar mais uma carta.") 
                else:
                    print("Uhmm. Acho que você não deveria comprar mais cartas.")
            n = input('Quer comprar outra carta?(sim/não): ')
            if n == 'sim':
                random.shuffle(deck)
                carta_nova = deck.pop()
                mao.append(carta_nova)
                print ('Sua carta é', carta_nova)
                if carta_nova == "J" or carta_nova == "Q" or carta_nova == "K":
                    soma_1+= 10
                elif carta_nova == "A":
                    if soma_1 >= 11:
                        soma_1+= 1
                    else: soma_1+= 11
                else:
                    soma_1 += carta_nova
                print ('Nova soma é', soma_1)
            if n == 'não':
                print ('Você está prestes a apostar com', soma_1)
                break
        print (mao_CPU)
        
        h = 0
        soma_CPU = 0
        while h < len(mao_CPU):
        carta_CPU = mao_CPU[h]
        if carta_CPU == "J" or carta_CPU == "Q" or carta_CPU == "K":
            soma_CPU+= 10
            h+=1
        elif carta_CPU == "A":
            if soma_CPU >= 11:
                soma_CPU+= 1
            else: 
                soma_CPU+= 11
            h+=1
        else: 
            soma_CPU += carta_CPU
            h+=1
        
        while soma_CPU < 17:
            random.shuffle(deck)
            carta_novaCPU = deck.pop()
            mao_CPU.append(carta_novaCPU)
            if carta_novaCPU == "J" or carta_novaCPU == "Q" or carta_novaCPU == "K":
                soma_CPU += 10
            elif carta_novaCPU == "A":
                if soma_CPU >= 11:
                    soma_CPU += 1
                else: 
                    soma_CPU += 1
            else:
                soma_CPU += carta_novaCPU
            print (carta_novaCPU)
        print ('A soma do dealer é',soma_CPU)
        
        
        total = 21 - soma_1
        total_CPU = 21 - soma_CPU
        
        if soma_1 == 21:
            d += 1.5*a
            print ('Ganhou sua aposta! Agora você possui', d)
            r = input('Quer jogar novamente?(sim/não): ')
            if r == 'sim':
                a = int(input('Insira um valor para apostar: '))
            if r == 'não':
                print ('Você saiu com', d)
                break
        elif soma_1 > 21:
            d = d - a
            print ('Perdeu! agora você possui', d)
            r = input('Quer jogar novamente?(sim/não): ')
            if r == 'sim':
                a = int(input('Insira um valor para apostar: '))
            if r == 'não':
                print ('Você saiu com', d)
                break
        elif soma_CPU > 21:
            d += 1.5*a
            print ('Ganhou sua aposta! Agora você possui', d)
            r = input('Quer jogar novamente?(sim/não): ')
            if r == 'sim':
                a = int(input('Insira um valor para apostar: '))
            if r == 'não':
                print ('Você saiu com', d)
                break   
        elif soma_CPU == 21:
            d = d - a
            print ('Perdeu! agora você possui', d)
            r = input('Quer jogar novamente?(sim/não): ')
            if r == 'sim':
                a = int(input('Insira um valor para apostar: '))
            if r == 'não':
                print ('Você saiu com', d)
                break
        else:
            if total > total_CPU:
                d = d - a
                print ('Perdeu! agora você possui', d)
                r = input('Quer jogar novamente?(sim/não): ')
                if r == 'sim':
                    a = int(input('Insira um valor para apostar: '))
                if r == 'não':
                    print ('Você saiu com', d)
                    break
            elif total == total_CPU:
                print ('Empate')
                r = input('Quer jogar novamente?(sim/não): ')
                if r == 'sim':
                    a = int(input('Insira um valor para apostar: '))
                if r == 'não':
                    print ('Você saiu com', d)
                    break
            else:
                d += 1.5*a
                print ('Ganhou sua aposta! Agora você possui', d)
                r = input('Quer jogar novamente?(sim/não): ')
                if r == 'sim':
                    a = int(input('Insira um valor para apostar: '))
                if r == 'não':
                    print ('Você saiu com', d)
                    break
#Jogada jogador 2
    aposta_2 = int(input("Ok {0}. Agora é sua vez, quanto você deseja apostar?: "))
    while d_jogador2 > 0 and d_jogador2 >= aposta_2:
            b = int(input('Com quantos baralhos deseja jogar?: '))
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4*b
            mao = []
            
            for i in range(2):
                random.shuffle(deck)
                carta = deck.pop()
                mao.append(carta)
            print (mao)
            
            j = 0
            soma_2 = 0
            while j < len(mao):
                carta = mao[j]
            if carta == "J" or carta == "Q" or carta == "K":
                soma_2 += 10
            elif carta == "A":
                if soma_2 >= 11:
                    soma_2 += 1
                else: 
                    soma_2+= 11
            else: 
                soma_2 += carta
            j+=1
            print ('Sua soma é', soma_2)

            mao_CPU = []
            for i in range(2):
                random.shuffle(deck)
                carta_CPU = deck.pop()
                mao_CPU.append(carta_CPU)

            print ("O dealer virou a carta", mao_CPU[0])

            if mao_CPU[0] == "Q" or mao_CPU[0] == "J" or mao_CPU[0] == "K" :
                mao_CPU[0] = 10
            elif mao_CPU[0] == "A":
                mao_CPU[0] = 11
            
            while soma_2 < 21:
                ajuda = input("Você deseja receber ajuda no que fazer?(sim/não)")

                if ajuda == "sim":
                    if soma_2 <= 11:
                        print("Uhmm. Acho que você deveria comprar mais uma carta.")
                    elif soma_2 >= 12 and mao_CPU[0] <= 6:
                        print("Uhmm. Acho que você não deveria comprar mais cartas.")
                    elif soma_2 >= 12 and soma_2 < 17 and mao_CPU[0] >= 7:
                        print("Uhmm. Acho que você deveria comprar mais uma carta.") 
                    else:
                        print("Uhmm. Acho que você não deveria comprar mais cartas.")
                n = input('Quer comprar outra carta?(sim/não): ')
                if n == 'sim':
                    random.shuffle(deck)
                    carta_nova = deck.pop()
                    mao.append(carta_nova)

                    print ('Sua carta é', carta_nova)
                    if carta_nova == "J" or carta_nova == "Q" or carta_nova == "K":
                        soma_2+= 10
                    elif carta_nova == "A":
                        if soma_2 >= 11:
                            soma_2 += 1
                        else: soma_2 += 11
                    else:
                        soma_2  += carta_nova
                    print ('Nova soma é', soma_2)
                if n == 'não':
                    print ('Você está prestes a apostar com', soma_2)
                    break
            print (mao_CPU)
            
            h = 0
            soma_CPU = 0
            while h < len(mao_CPU):
            carta_CPU = mao_CPU[h]
            if carta_CPU == "J" or carta_CPU == "Q" or carta_CPU == "K":
                soma_CPU+= 10
                h+=1
            elif carta_CPU == "A":
                if soma_CPU >= 11:
                    soma_CPU+= 1
                else: 
                    soma_CPU+= 11
                h+=1
            else: 
                soma_CPU += carta_CPU
                h+=1
            
            while soma_CPU < 17:
                random.shuffle(deck)
                carta_novaCPU = deck.pop()
                mao_CPU.append(carta_novaCPU)
                if carta_novaCPU == "J" or carta_novaCPU == "Q" or carta_novaCPU == "K":
                    soma_CPU += 10
                elif carta_novaCPU == "A":
                    if soma_CPU >= 11:
                        soma_CPU += 1
                    else: 
                        soma_CPU += 1
                else:
                    soma_CPU += carta_novaCPU
                print (carta_novaCPU)
            print ('A soma do dealer é',soma_CPU)
            
            
            total = 21 - soma_2
            total_CPU = 21 - soma_CPU
            
            if soma_2 == 21:
                d += 1.5*a
                print ('Ganhou sua aposta! Agora você possui', d)
                r = input('Quer jogar novamente?(sim/não): ')
                if r == 'sim':
                    a = int(input('Insira um valor para apostar: '))
                if r == 'não':
                    print ('Você saiu com', d)
                    break
            elif soma_2 > 21:
                d = d - a
                print ('Perdeu! agora você possui', d)
                r = input('Quer jogar novamente?(sim/não): ')
                if r == 'sim':
                    a = int(input('Insira um valor para apostar: '))
                if r == 'não':
                    print ('Você saiu com', d)
                    break
            elif soma_CPU > 21:
                d += 1.5*a
                print ('Ganhou sua aposta! Agora você possui', d)
                r = input('Quer jogar novamente?(sim/não): ')
                if r == 'sim':
                    a = int(input('Insira um valor para apostar: '))
                if r == 'não':
                    print ('Você saiu com', d)
                    break   
            elif soma_CPU == 21:
                d = d - a
                print ('Perdeu! agora você possui', d)
                r = input('Quer jogar novamente?(sim/não): ')
                if r == 'sim':
                    a = int(input('Insira um valor para apostar: '))
                if r == 'não':
                    print ('Você saiu com', d)
                    break
            else:
                if total > total_CPU:
                    d = d - a
                    print ('Perdeu! agora você possui', d)
                    r = input('Quer jogar novamente?(sim/não): ')
                    if r == 'sim':
                        a = int(input('Insira um valor para apostar: '))
                    if r == 'não':
                        print ('Você saiu com', d)
                        break
                elif total == total_CPU:
                    print ('Empate')
                    r = input('Quer jogar novamente?(sim/não): ')
                    if r == 'sim':
                        a = int(input('Insira um valor para apostar: '))
                    if r == 'não':
                        print ('Você saiu com', d)
                        break
                else:
                    d += 1.5*a
                    print ('Ganhou sua aposta! Agora você possui', d)
                    r = input('Quer jogar novamente?(sim/não): ')
                    if r == 'sim':
                        a = int(input('Insira um valor para apostar: '))
                    if r == 'não':
                        print ('Você saiu com', d)
                        break
#Jogo para um
if dois_jogadores == "não": 
    d = 1000
    a = int(input('Insira um valor para apostar: '))

    while d > 0 and d >= a:
        b = int(input('Com quantos baralhos deseja jogar?: '))
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]*4*b
        mao = []
        
        for i in range(2):
            random.shuffle(deck)
            carta = deck.pop()
            mao.append(carta)
        print (mao)
        
        j = 0
        soma = 0
        while j < len(mao):
            carta = mao[j]
        if carta == "J" or carta == "Q" or carta == "K":
            soma+= 10
        elif carta == "A":
            if soma >= 11:
                soma+= 1
            else: 
                soma+= 11
        else: 
            soma += carta
        j+=1
        print ('Sua soma é', soma)

        mao_CPU = []
        for i in range(2):
            random.shuffle(deck)
            carta_CPU = deck.pop()
            mao_CPU.append(carta_CPU)

        print ("O dealer virou a carta", mao_CPU[0])

        if mao_CPU[0] == "Q" or mao_CPU[0] == "J" or mao_CPU[0] == "K" :
            mao_CPU[0] = 10
        elif mao_CPU[0] == "A":
            mao_CPU[0] = 11
        
        while soma < 21:
            ajuda = input("Você deseja receber ajuda no que fazer?(sim/não)")

            if ajuda == "sim":
                if soma <= 11:
                    print("Uhmm. Acho que você deveria comprar mais uma carta.")
                elif soma >= 12 and mao_CPU[0] <= 6:
                    print("Uhmm. Acho que você não deveria comprar mais cartas.")
                elif soma >= 12 and soma < 17 and mao_CPU[0] >= 7:
                    print("Uhmm. Acho que você deveria comprar mais uma carta.") 
                else:
                    print("Uhmm. Acho que você não deveria comprar mais cartas.")
            n = input('Quer comprar outra carta?(sim/não): ')
            if n == 'sim':
                random.shuffle(deck)
                carta_nova = deck.pop()
                mao.append(carta_nova)
                print ('Sua carta é', carta_nova)
                if carta_nova == "J" or carta_nova == "Q" or carta_nova == "K":
                    soma+= 10
                elif carta_nova == "A":
                    if soma >= 11:
                        soma+= 1
                    else: soma+= 11
                else:
                    soma += carta_nova
                print ('Nova soma é', soma)
            if n == 'não':
                print ('Você está prestes a apostar com', soma)
                break
        print (mao_CPU)
        
        h = 0
        soma_CPU = 0
        while h < len(mao_CPU):
            carta_CPU = mao_CPU[h]
        if carta_CPU == "J" or carta_CPU == "Q" or carta_CPU == "K":
            soma_CPU+= 10
            h+=1
        elif carta_CPU == "A":
            if soma_CPU >= 11:
                soma_CPU+= 1
            else: 
                soma_CPU+= 11
            h+=1
        else: 
            soma_CPU += carta_CPU
            h+=1
        
        while soma_CPU < 17:
            random.shuffle(deck)
            carta_novaCPU = deck.pop()
            mao_CPU.append(carta_novaCPU)
            if carta_novaCPU == "J" or carta_novaCPU == "Q" or carta_novaCPU == "K":
                soma_CPU += 10
            elif carta_novaCPU == "A":
                if soma_CPU >= 11:
                    soma_CPU += 1
                else: 
                    soma_CPU += 1
            else:
                soma_CPU += carta_novaCPU
            print (carta_novaCPU)
        print ('A soma do dealer é',soma_CPU)
        
        
        total = 21 - soma
        total_CPU = 21 - soma_CPU
        
        if soma == 21:
            d += 1.5*a
            print ('Ganhou sua aposta! Agora você possui', d)
            r = input('Quer jogar novamente?(sim/não): ')
            if r == 'sim':
                a = int(input('Insira um valor para apostar: '))
            if r == 'não':
                print ('Você saiu com', d)
                break
        elif soma > 21:
            d = d - a
            print ('Perdeu! agora você possui', d)
            r = input('Quer jogar novamente?(sim/não): ')
            if r == 'sim':
                a = int(input('Insira um valor para apostar: '))
            if r == 'não':
                print ('Você saiu com', d)
                break
        elif soma_CPU > 21:
            d += 1.5*a
            print ('Ganhou sua aposta! Agora você possui', d)
            r = input('Quer jogar novamente?(sim/não): ')
            if r == 'sim':
                a = int(input('Insira um valor para apostar: '))
            if r == 'não':
                print ('Você saiu com', d)
                break   
        elif soma_CPU == 21:
            d = d - a
            print ('Perdeu! agora você possui', d)
            r = input('Quer jogar novamente?(sim/não): ')
            if r == 'sim':
                a = int(input('Insira um valor para apostar: '))
            if r == 'não':
                print ('Você saiu com', d)
                break
        else:
            if total > total_CPU:
                d = d - a
                print ('Perdeu! agora você possui', d)
                r = input('Quer jogar novamente?(sim/não): ')
                if r == 'sim':
                    a = int(input('Insira um valor para apostar: '))
                if r == 'não':
                    print ('Você saiu com', d)
                    break
            elif total == total_CPU:
                print ('Empate')
                r = input('Quer jogar novamente?(sim/não): ')
                if r == 'sim':
                    a = int(input('Insira um valor para apostar: '))
                if r == 'não':
                    print ('Você saiu com', d)
                    break
            else:
                d += 1.5*a
                print ('Ganhou sua aposta! Agora você possui', d)
                r = input('Quer jogar novamente?(sim/não): ')
                if r == 'sim':
                    a = int(input('Insira um valor para apostar: '))
                if r == 'não':
                    print ('Você saiu com', d)
                    break
        
#C:\Users\luisf\OneDrive\Área de Trabalho\Insper\1°Sem
#\DesSoft\Avaliações\EP's